import torch
import nn_models.Models as M
import time
net = M.AdmiralNetSplinePredictor()
a = torch.rand(1,1,25,200)
print(net.hidden_decoder(a).shape)
net = net.cuda(0)
im = torch.rand(1,5,3,66,200)
im = im.cuda(0)
net=net.eval()
print("Running net")
tick = time.time()
out = net(im)
tock = time.time()
print(out.shape)
print("Got prediction in %f seconds"%(tock-tick))