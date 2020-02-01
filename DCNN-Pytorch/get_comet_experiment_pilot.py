import comet_ml
import torch
import os
import argparse
from comet_ml.api import API, APIExperiment
import yaml
import torch.nn as NN
import numpy as np
import torch.utils.data as data_utils
import deepracing_models.data_loading.proto_datasets as PD
from tqdm import tqdm as tqdm
import deepracing_models.nn_models.LossFunctions as loss_functions
import deepracing_models.nn_models.Models
parser = argparse.ArgumentParser(description="Download experiment from Comet.ml")
parser.add_argument("experiment_key", type=str, help="Experiment key to grab from comet.")
parser.add_argument("--restkey", type=str, required=False, default=None, help="Experiment key to grab from comet.")
parser.add_argument("--epoch_number", type=int, required=False, default=100, help="Experiment key to grab from comet.")
parser.add_argument("--output_directory", type=str, required=False, default=".", help="Where to put the config and data files.")

#XMUs9uI19KQNdYrQhuXPnAfpB
args = parser.parse_args()
experiment_key = args.experiment_key
epoch_number = args.epoch_number
restkey = args.restkey
output_directory = os.path.join(args.output_directory, experiment_key + "_from_comet")
if not os.path.isdir(output_directory):
    os.makedirs(output_directory)
if restkey is None:
    api = API()
else:
    api = API(rest_api_key=restkey)
experiment : APIExperiment = api.get_experiment("electric-turtle", "deepracingpilotnet", experiment_key)
assetlist = experiment.get_asset_list()
assetdict = {d['fileName']: d['assetId'] for d in assetlist}

#get network weight file
weightfilename = "pilotnet_epoch_%d_params.pt" %(epoch_number,)

print("Getting network weights from comet")
params_binary = experiment.get_asset(assetdict[weightfilename])


outputweightfile = os.path.join(output_directory,weightfilename)
with open(outputweightfile, 'wb') as f:
    f.write(params_binary)

#get parameters
parameters_summary = experiment.get_parameters_summary()
configin = {d["name"] : d["valueCurrent"] for d in parameters_summary}
config = {}
config["image_size"] = np.fromstring(configin["image_size"].replace(" ","")[1:-1],sep=',').astype(np.int32).tolist()
config["input_channels"] = int( configin["input_channels"] )
config["output_dimension"] = int( configin["output_dimension"] )
print(config)


outputconfigfile = os.path.join(output_directory,"config.yaml")
with open(outputconfigfile, 'w') as f:
    yaml.dump(config,stream=f,Dumper=yaml.SafeDumper)

input_channels = config["input_channels"]
output_dimension = config["output_dimension"]
net = deepracing_models.nn_models.Models.PilotNet( input_channels=input_channels, output_dim=output_dimension ) 
net = net.double()
with open(outputweightfile, 'rb') as f:
    net.load_state_dict(torch.load(f, map_location=torch.device("cpu")))