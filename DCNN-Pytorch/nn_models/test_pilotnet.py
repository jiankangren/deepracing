import cv2
import numpy as np
import nn_models
import data_loading.image_loading as il
import nn_models.Models as models
import data_loading.data_loaders as loaders
import numpy.random
import torch, random
import torch.nn as nn 
import torch.optim as optim
from tqdm import tqdm as tqdm
import pickle
from datetime import datetime
import os
import string
import argparse
from random import randint
from datetime import datetime
import imutils.annotation_utils
from data_loading.image_loading import load_image
import torchvision.transforms as transforms

def main():
    parser = argparse.ArgumentParser(description="Test AdmiralNet")
    parser.add_argument("--model_file", type=str, required=True)
    parser.add_argument("--annotation_file", type=str, required=True)
    parser.add_argument("--plot", action="store_true")
    args = parser.parse_args()
    
    annoation_dir, annotation_file = os.path.split(args.annotation_file)
    model_dir, model_file = os.path.split(args.model_file)
    config_path = os.path.join(model_dir,'config.pkl')
    config_file = open(config_path,'rb')
    config = pickle.load(config_file)
    print(config)
   # return

    gpu = int(config['gpu'])
    use_float32 = bool(config['use_float32'])
    label_scale = float(config['label_scale'])
    size = (66,200)
    prefix, _ = annotation_file.split(".")
    prefix = prefix + config['file_prefix']

    network = models.PilotNet()
    state_dict = torch.load(args.model_file)
    network.load_state_dict(state_dict)
    print(network)
    if(label_scale == 1.0):
        label_transformation = None
    else:
        label_transformation = transforms.Compose([transforms.Lambda(lambda inputs: inputs.mul(label_scale))])
    if(use_float32):
        network.float()
        trainset = loaders.F1Dataset(annoation_dir,annotation_file,(66,200), use_float32=True, label_transformation = label_transformation)
    else:
        network.double()
        trainset = loaders.F1Dataset(annoation_dir, annotation_file,(66,200), label_transformation = label_transformation)
    
    if(gpu>=0):
        network = network.cuda(gpu)
    if((not os.path.isfile("./" + prefix+"_images.pkl")) or (not os.path.isfile("./" + prefix+"_annotations.pkl"))):
        trainset.read_files()
        trainset.write_pickles(prefix+"_images.pkl",prefix+"_annotations.pkl")
    else:  
        trainset.read_pickles(prefix+"_images.pkl",prefix+"_annotations.pkl")
    mean,stdev = trainset.statistics()
    print(mean)
    print(stdev)
    img_transformation = transforms.Compose([transforms.Normalize(mean,stdev)])
    trainset.img_transformation = img_transformation
    loader = torch.utils.data.DataLoader(trainset, batch_size = 1, shuffle = False, num_workers = 0)
    cum_diff = 0.0
    t = tqdm(enumerate(loader))
    network.eval()
    predictions=[]
    ground_truths=[]
    losses=[]
    criterion = nn.MSELoss()
    if(gpu>=0):
        criterion = criterion.cuda(gpu)
    for idx,(inputs, labels) in t:
        if(gpu>=0):
            inputs = inputs.cuda(gpu)
            labels = labels.cuda(gpu)
        pred = torch.div(network(inputs),label_scale)
        if pred.shape[1] == 1:
            angle = pred.item()
            ground_truth = labels.item()
        else:
            angle = pred.squeeze()[0].item()
            ground_truth = labels.squeeze()[0].item()
        predictions.append(angle)
        ground_truths.append(ground_truth)
        loss = criterion(pred, labels)
        losses.append(loss.item())
        t.set_postfix(angle = angle, ground_truth = ground_truth)
       # print("Ground Truth: %f. Prediction: %f.\n" %(scaled_ground_truth, scaled_angle))
        '''
        M = cv2.getRotationMatrix2D((wheelrows/2,wheelcols/2),scaled_angle,1)
        wheel_rotated = cv2.warpAffine(wheel,M,(wheelrows,wheelcols))
        overlayed = imutils.annotation_utils.overlay_image(background,wheel_rotated,x,y)
        name, _ = filename.split(".")
        _,_,img_num_str = name.split("_")
        img_num_str = img_num_str.replace("\n","")
        output_path = os.path.join(args.output_folder,'overlayed_image_' + img_num_str + ".jpg")
        cv2.imwrite(output_path,overlayed)
        videoout.write(overlayed)
        '''
    predictions_array = np.array(predictions)
    ground_truths_array = np.array(ground_truths)
    diffs = np.subtract(predictions_array,ground_truths_array)
    rms = np.mean(np.array(losses))
    print("RMS Error: ", rms)
    if args.plot:
        from scipy import stats
        import matplotlib.pyplot as plt
        t = np.linspace(0,len(loader)-1,len(loader))
        plt.plot(t,predictions_array,'r')
        plt.plot(t,ground_truths_array,'b')
        plt.show()
if __name__ == '__main__':
    main()
