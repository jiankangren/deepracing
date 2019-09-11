import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim
import torch.utils.data as data
import numpy as np
import torch
import torchvision.models as visionmodels
import torchvision.models.vgg
import sys
class ResNetAdapter(nn.Module):
    def __init__(self, output_dimension = 1, pretrained = True):
        super(ResNetAdapter, self).__init__()
        resnet_model = visionmodels.resnet152(pretrained = pretrained)
        self.features = nn.Sequential(*list(resnet_model.children())[:-2])
        self.classifier = nn.Sequential(*[nn.Linear(43008, 2048),\
                        nn.Linear(2048, 1024),\
                        nn.Linear(1024, 128),\
                        nn.Linear(128, output_dimension)])
    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        predictions = self.classifier(x)
        return predictions

class PilotNet(nn.Module):
    """PyTorch Implementation of NVIDIA's PilotNet"""
    def __init__(self, input_channels = 3, output_dim = 1):
        super(PilotNet, self).__init__()
        # Convolutional layers.
        self.output_size = output_dim
        self.conv1 = nn.Conv2d(input_channels, 24, kernel_size=5, stride=2)
        self.conv2 = nn.Conv2d(24, 36, kernel_size=5, stride=2)
        self.conv3 = nn.Conv2d(36, 48, kernel_size=5, stride=2)
        self.conv4 = nn.Conv2d(48, 64, kernel_size=3)
        self.conv5 = nn.Conv2d(64, 64, kernel_size=3)
        # Linear layers.
        self.fc1 = nn.Linear(64*1*18, 100)
        self.fc2 = nn.Linear(100, 50)
        self.fc3 = nn.Linear(50, 10)
        self.prediction_layer = nn.Linear(10, self.output_size)

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.conv5(out)
        # This flattens the output of the previous layer into a vector.
        out = out.view(out.size(0), -1) 
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        out = self.prediction_layer(out)
        #out = out.unsqueeze(2)
        #print(out.size())
        return out
class CommandantNet(nn.Module):
    def __init__(self, sequence_length=25, context_length = 25, hidden_dim = 100, use_float32 = False, gpu = -1, optical_flow = False):
        super(CommandantNet, self).__init__()
        self.gpu=gpu
        self.use_float32=use_float32
        # Convolutional layers.
        self.output_size = 1
        if optical_flow:
            self.input_channels = 2
        else:
            self.input_channels = 3
        self.conv1 = nn.Conv2d(self.input_channels, 12, kernel_size=5, stride=2)
        self.conv2 = nn.Conv2d(12, 24, kernel_size=3, stride=2)
        self.conv3 = nn.Conv2d(24, 36, kernel_size=3)
        self.pool1 = nn.MaxPool2d(3,3)
        self.conv4 = nn.Conv2d(36, 36, kernel_size=3)
        self.conv5 = nn.Conv2d(36, 24, kernel_size=3)
        self.conv6 = nn.Conv2d(24, 12, kernel_size=3)
        self.pool2 = nn.MaxPool2d(2,2)
        #batch norm layers
        self.Norm_1 = nn.BatchNorm2d(12)
        self.Norm_2 = nn.BatchNorm2d(24)
        self.Norm_3 = nn.BatchNorm2d(36) 
        self.Norm_4 = nn.BatchNorm2d(36)
        self.Norm_5 = nn.BatchNorm2d(24)
        
        #recurrent layers
        self.hidden_dim = hidden_dim
        self.sequence_length=sequence_length
        self.context_length = context_length
        self.feature_length = 157
        
        self.lstm = nn.LSTM(self.feature_length, hidden_dim, batch_first = True)

        # Linear layers.
        self.prediction_layer = nn.Linear(hidden_dim, self.output_size)
    
        #activations
        self.relu = nn.ReLU()

    def forward(self, x, previous_control):
        #resize for convolutional layers
        batch_size = x.shape[0]
        x = x.view(-1, self.input_channels, 125,400) 
        x = self.conv1(x)
        x = self.Norm_1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.Norm_2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.Norm_3(x)
        x = self.relu(x)
        x = self.pool1(x)

        x = self.conv4(x)
        x = self.Norm_4(x)
        x = self.relu(x)
        x = self.conv5(x)
        x = self.Norm_5(x)
        x = self.relu(x)
        x = self.conv6(x)
        x = self.relu(x)
        x = self.pool2(x)

        # Unpack for the LSTM.
        x = x.view(batch_size, self.context_length, self.feature_length-1) 
        x = torch.cat((x,previous_control),2)
        x, init_hidden = self.lstm(x) 
        if(self.use_float32):
            zeros = torch.zeros([batch_size, self.sequence_length, self.feature_length], dtype=torch.float32)
                
        else:
            zeros = torch.zeros([batch_size, self.sequence_length, self.feature_length], dtype=torch.float64)
        if(self.gpu>=0):
            zeros = zeros.cuda(self.gpu)
        x, final_hidden = self.lstm(zeros, init_hidden)
        predictions = self.prediction_layer(x)
        return predictions
class CNNLSTM(nn.Module):
    def __init__(self, input_channels=3, output_dimension = 3, context_length=5, sequence_length=1, hidden_dim = 100):
        super(CNNLSTM, self).__init__()
        #self.input_channels = 5
        self.input_channels = input_channels
        # Convolutional layers.

        self.output_size = output_dimension
        self.conv1 = nn.Conv2d(self.input_channels, 24, kernel_size=5, stride=2)
        self.conv2 = nn.Conv2d(24, 36, kernel_size=5, stride=2)
        self.conv3 = nn.Conv2d(36, 48, kernel_size=5, stride=2)
        self.conv4 = nn.Conv2d(48, 64, kernel_size=3)
        self.conv5 = nn.Conv2d(64, 64, kernel_size=3)

        #batch norm layers
        self.Norm_1 = nn.BatchNorm2d(24)
        self.Norm_2 = nn.BatchNorm2d(36)
        self.Norm_3 = nn.BatchNorm2d(48) 
        self.Norm_4 = nn.BatchNorm2d(64)

        #recurrent layers
        self.img_features = 1*64*18
        self.feature_length = (1*64*18)
        self.hidden_dim = hidden_dim
        self.context_length = context_length
        self.sequence_length = sequence_length
        
        self.rnn_init_hidden = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=True)
        self.rnn_init_cell = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=True)

        self.rnn = nn.LSTM(self.feature_length, hidden_dim, batch_first = True)
 
        # Linear layers.
        self.prediction_layer = nn.Linear(hidden_dim, self.output_size)

        #activations
        self.relu = nn.ReLU()

        self.projector_input = torch.nn.Parameter(torch.normal(0, 1, size=(self.sequence_length, self.feature_length)), requires_grad=True)
        
               
    def forward(self, x):
        #resize for convolutional layers
        batch_size = x.shape[0]
      #  print(x.shape)
        x1 = x.view(-1, self.input_channels, 66, 200) 
        #print(x1.shape)
        x2 = self.conv1(x1)
        x3 = self.Norm_1(x2)
        x4 = self.relu(x3)
        x5 = self.conv2(x4)
        x6 = self.Norm_2(x5)
        x7 = self.relu(x6)
        x8 = self.conv3(x7)
        x9 = self.Norm_3(x8)
        x10 = self.relu(x9)
        x11 = self.conv4(x10)
        x12 = self.Norm_4(x11)
        x13 = self.relu(x12)
        x14 = self.conv5(x13)
        x15 = self.relu(x14)
        #maps=[x1,x2,x3,x4,x5]
        # Unpack for the RNN.
       # print(x15.shape)
        x16 = x15.view(batch_size, self.context_length, self.img_features)

        rnn_init_hidden = self.rnn_init_hidden.repeat(1,batch_size,1)
        rnn_init_cell = self.rnn_init_cell.repeat(1,batch_size,1)
        _, (new_hidden, new_cell) = self.rnn(x16, (rnn_init_hidden,  rnn_init_cell) )     
     #   print(new_hidden[0].shape)   
      #  print(init_hidden[1].shape)
        
        projector = self.projector_input.repeat(batch_size,1,1)
        x17, final_hidden = self.rnn( projector, (new_hidden, new_cell) )

        predictions = self.prediction_layer(x17)

        return predictions


class AdmiralNetVelocityPredictor(nn.Module):
    def __init__(self, input_channels=3, sequence_length=10, context_length = 15, \
                 hidden_dim = 100, num_recurrent_layers = 1, temporal_conv_feature_factor = 1, \
                     learnable_initial_state=False):
        super(AdmiralNetVelocityPredictor, self).__init__()
        self.imsize = (66,200)
        #self.input_channels = 5
        self.input_channels = input_channels
        # Convolutional layers.

        self.conv1 = nn.Conv2d(self.input_channels, 24, kernel_size=5, stride=2)
        self.conv2 = nn.Conv2d(24, 36, kernel_size=5, stride=2)
        self.conv3 = nn.Conv2d(36, 48, kernel_size=5, stride=2)
        self.conv4 = nn.Conv2d(48, 64, kernel_size=3)
        self.conv5 = nn.Conv2d(64, 64, kernel_size=3)

        #batch norm layers
        self.Norm_1 = nn.BatchNorm2d(24)
        self.Norm_2 = nn.BatchNorm2d(36)
        self.Norm_3 = nn.BatchNorm2d(48) 
        self.Norm_4 = nn.BatchNorm2d(64)

        #recurrent layers
        self.img_features = 1*64*18
        self.feature_length = self.img_features
        self.hidden_dim = hidden_dim
        self.sequence_length = sequence_length
        self.context_length = context_length

        #projection encoder
        self.conv3d1 = nn.Conv3d(input_channels, 10, kernel_size=(5,3,3), stride = (1,2,2), padding=(2,0,0) )
        self.conv3d2 = nn.Conv3d(10, 20, kernel_size=(5,3,3), stride = (1,2,2), padding=(2,0,0))
        self.conv3d3 = nn.Conv3d(20, 40, kernel_size=(3,3,3), stride = (1,2,2), padding=(1,0,0))
        final_3d_conv_channels = temporal_conv_feature_factor*self.sequence_length
        self.conv3d4 = nn.Conv3d(40, final_3d_conv_channels, kernel_size=(3,3,3), stride = (1,1,1), padding=(1,0,0))
        self.projection_features = temporal_conv_feature_factor * self.context_length * 5 * 22
        self.projection_layer = nn.Linear(self.projection_features, self.feature_length)

        #project encoder normalizers
        
        self.Norm3d_1 = nn.BatchNorm3d(10)
        self.Norm3d_2 = nn.BatchNorm3d(20)
        self.Norm3d_3 = nn.BatchNorm3d(40) 
        self.Norm3d_4 = nn.BatchNorm3d(final_3d_conv_channels)

        self.linear_rnn = nn.LSTM(self.feature_length, hidden_dim, batch_first = True, num_layers = num_recurrent_layers)
        self.angular_rnn = nn.LSTM(self.feature_length, hidden_dim, batch_first = True, num_layers = num_recurrent_layers)

        self.linear_rnn_init_hidden = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)
        self.linear_rnn_init_cell = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)

        self.angular_rnn_init_hidden = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)
        self.angular_rnn_init_cell = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)
    
        # Linear layers.
        self.linear_prediction_layer1 = nn.Linear(hidden_dim, int(round(hidden_dim/2)))
        self.linear_prediction_layer2 = nn.Linear(int(round(hidden_dim/2)), int(round(hidden_dim/4)))
        self.linear_prediction_layer3 = nn.Linear(int(round(hidden_dim/4)), 3)


        self.angular_prediction_layer1 = nn.Linear(hidden_dim, int(round(hidden_dim/2)))
        self.angular_prediction_layer2 = nn.Linear(int(round(hidden_dim/2)), int(round(hidden_dim/4)))
        self.angular_prediction_layer3 = nn.Linear(int(round(hidden_dim/4)), 3)

        #activations
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()

    def forward(self, x):
        #resize for convolutional layers
        batch_size = x.shape[0]
        y = self.conv3d1( x.view(batch_size, self.input_channels, self.context_length, self.imsize[0], self.imsize[1]) )
        y = self.Norm3d_1(y)
        y = self.relu(y)    
        #print(y.shape)
        x0 = x.view(-1, self.input_channels, self.imsize[0], self.imsize[1]) 
        x1 = self.conv1(x0)
        x2 = self.Norm_1(x1)
        x3 = self.relu(x2)
        x4 = self.conv2(x3)
        x5 = self.Norm_2(x4)
        x6 = self.relu(x5)
        x7 = self.conv3(x6)
        x8 = self.Norm_3(x7)
        x9 = self.relu(x8)
        x10 = self.conv4(x9)
        x11 = self.Norm_4(x10)
        x12 = self.relu(x11)
        x13 = self.conv5(x12)
        x14 = self.relu(x13)
        # Unpack for the RNN.
        x15 = x14.view(batch_size , self.context_length , self.img_features)

        linear_rnn_init_hidden = self.linear_rnn_init_hidden.repeat(1,batch_size,1)
        linear_rnn_init_cell = self.linear_rnn_init_cell.repeat(1,batch_size,1)
        _, (linear_new_hidden, linear_new_cell) = self.linear_rnn(x15, (linear_rnn_init_hidden,  linear_rnn_init_cell) )
        
        angular_rnn_init_hidden = self.angular_rnn_init_hidden.repeat(1,batch_size,1)
        angular_rnn_init_cell = self.angular_rnn_init_cell.repeat(1,batch_size,1)
        _, (angular_new_hidden, angular_new_cell) = self.angular_rnn(x15, (angular_rnn_init_hidden,  angular_rnn_init_cell) )
        # print(new_hidden.shape)
        # print(new_hidden.dtype)
        # print(new_cell.shape)
        # print(new_cell.dtype)
      
        y = self.conv3d2(y)
        y = self.Norm3d_2(y)
        y = self.relu(y) 

        y = self.conv3d3(y) 
        y = self.Norm3d_3(y)
        y = self.relu(y) 

        y = self.conv3d4(y)
       # print(y.shape)
        y = self.Norm3d_4(y)
        y = self.relu(y) 
        #print(y.shape)
        y = y.view(batch_size, self.sequence_length , self.projection_features)
        y = self.projection_layer(y)

        x_linear, (final_hidden_position, final_cell_position) = self.linear_rnn(  y , (linear_new_hidden, linear_new_cell) )
        x_angular, (final_hidden_rotation, final_cell_rotation) = self.angular_rnn(  y , (angular_new_hidden, angular_new_cell) )
       # print(x_position.shape)
        position_predictions1 = self.linear_prediction_layer1(x_linear)
        position_predictions1 = self.tanh(position_predictions1)
        position_predictions2 = self.linear_prediction_layer2(position_predictions1)
        position_predictions2 = self.tanh(position_predictions2)
        position_predictions = self.linear_prediction_layer3(position_predictions2)


        rotation_predictions1 = self.angular_prediction_layer1(x_angular)
        rotation_predictions1 = self.tanh(rotation_predictions1)
        rotation_predictions2 = self.angular_prediction_layer2(rotation_predictions1)
        rotation_predictions2 = self.tanh(rotation_predictions2)
        rotation_predictions = self.angular_prediction_layer3(rotation_predictions2)

        return position_predictions, rotation_predictions

class AdmiralNetPosePredictor(nn.Module):
    def __init__(self, cell='lstm', input_channels=3, sequence_length=10, context_length = 15, \
                 hidden_dim = 100, num_recurrent_layers = 1, temporal_conv_feature_factor = 1, \
                     learnable_initial_state=False):
        super(AdmiralNetPosePredictor, self).__init__()
        self.imsize = (66,200)
        #self.input_channels = 5
        self.input_channels = input_channels
        # Convolutional layers.

        self.conv1 = nn.Conv2d(self.input_channels, 24, kernel_size=5, stride=2)
        self.conv2 = nn.Conv2d(24, 36, kernel_size=5, stride=2)
        self.conv3 = nn.Conv2d(36, 48, kernel_size=5, stride=2)
        self.conv4 = nn.Conv2d(48, 64, kernel_size=3)
        self.conv5 = nn.Conv2d(64, 64, kernel_size=3)

        #batch norm layers
        self.Norm_1 = nn.BatchNorm2d(24)
        self.Norm_2 = nn.BatchNorm2d(36)
        self.Norm_3 = nn.BatchNorm2d(48) 
        self.Norm_4 = nn.BatchNorm2d(64)

        #recurrent layers
        self.img_features = 1*64*18
        self.feature_length = self.img_features
        self.hidden_dim = hidden_dim
        self.sequence_length = sequence_length
        self.context_length = context_length

        #projection encoder
        self.conv3d1 = nn.Conv3d(input_channels, 10, kernel_size=(5,3,3), stride = (1,2,2), padding=(2,0,0) )
        self.conv3d2 = nn.Conv3d(10, 20, kernel_size=(5,3,3), stride = (1,2,2), padding=(2,0,0))
        self.conv3d3 = nn.Conv3d(20, 40, kernel_size=(3,3,3), stride = (1,2,2), padding=(1,0,0))
        final_3d_conv_channels = temporal_conv_feature_factor*self.sequence_length
        self.conv3d4 = nn.Conv3d(40, final_3d_conv_channels, kernel_size=(3,3,3), stride = (1,1,1), padding=(1,0,0))
        self.projection_features = temporal_conv_feature_factor * self.context_length * 5 * 22
        self.projection_layer = nn.Linear(self.projection_features, self.feature_length)

        #project encoder normalizers
        
        self.Norm3d_1 = nn.BatchNorm3d(10)
        self.Norm3d_2 = nn.BatchNorm3d(20)
        self.Norm3d_3 = nn.BatchNorm3d(40) 
        self.Norm3d_4 = nn.BatchNorm3d(final_3d_conv_channels)

        self.position_rnn = nn.LSTM(self.feature_length, hidden_dim, batch_first = True, num_layers = num_recurrent_layers)
        self.rotation_rnn = nn.LSTM(self.feature_length, hidden_dim, batch_first = True, num_layers = num_recurrent_layers)

        self.position_rnn_init_hidden = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)
        self.position_rnn_init_cell = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)

        self.rotation_rnn_init_hidden = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)
        self.rotation_rnn_init_cell = torch.nn.Parameter(torch.normal(0, 1, size=(1,self.hidden_dim)), requires_grad=learnable_initial_state)
    
        # Linear layers.
        self.position_prediction_layer1 = nn.Linear(hidden_dim, int(round(hidden_dim/2)))
        self.position_prediction_layer2 = nn.Linear(int(round(hidden_dim/2)), int(round(hidden_dim/4)))
        self.position_prediction_layer3 = nn.Linear(int(round(hidden_dim/4)), 3)


        self.rotation_prediction_layer1 = nn.Linear(hidden_dim, int(round(hidden_dim/2)))
        self.rotation_prediction_layer2 = nn.Linear(int(round(hidden_dim/2)), int(round(hidden_dim/4)))
        self.rotation_prediction_layer3 = nn.Linear(int(round(hidden_dim/4)), 4)

        #activations
        self.relu = nn.ReLU()
        self.tanh = nn.Tanh()

    def forward(self, x):
        #resize for convolutional layers
        batch_size = x.shape[0]
        y = self.conv3d1( x.view(batch_size, self.input_channels, self.context_length, self.imsize[0], self.imsize[1]) )
        y = self.Norm3d_1(y)
        y = self.relu(y)    
        #print(y.shape)
        x0 = x.view(-1, self.input_channels, self.imsize[0], self.imsize[1]) 
        x1 = self.conv1(x0)
        x2 = self.Norm_1(x1)
        x3 = self.relu(x2)
        x4 = self.conv2(x3)
        x5 = self.Norm_2(x4)
        x6 = self.relu(x5)
        x7 = self.conv3(x6)
        x8 = self.Norm_3(x7)
        x9 = self.relu(x8)
        x10 = self.conv4(x9)
        x11 = self.Norm_4(x10)
        x12 = self.relu(x11)
        x13 = self.conv5(x12)
        x14 = self.relu(x13)
        # Unpack for the RNN.
        x15 = x14.view(batch_size , self.context_length , self.img_features)

        position_rnn_init_hidden = self.position_rnn_init_hidden.repeat(1,batch_size,1)
        position_rnn_init_cell = self.position_rnn_init_cell.repeat(1,batch_size,1)
        _, (position_new_hidden, position_new_cell) = self.position_rnn(x15, (position_rnn_init_hidden,  position_rnn_init_cell) )
        
        rotation_rnn_init_hidden = self.rotation_rnn_init_hidden.repeat(1,batch_size,1)
        rotation_rnn_init_cell = self.rotation_rnn_init_cell.repeat(1,batch_size,1)
        _, (rotation_new_hidden, rotation_new_cell) = self.rotation_rnn(x15, (rotation_rnn_init_hidden,  rotation_rnn_init_cell) )
        # print(new_hidden.shape)
        # print(new_hidden.dtype)
        # print(new_cell.shape)
        # print(new_cell.dtype)
      
        y = self.conv3d2(y)
        y = self.Norm3d_2(y)
        y = self.relu(y) 

        y = self.conv3d3(y) 
        y = self.Norm3d_3(y)
        y = self.relu(y) 

        y = self.conv3d4(y)
       # print(y.shape)
        y = self.Norm3d_4(y)
        y = self.relu(y) 
        #print(y.shape)
        y = y.view(batch_size, self.sequence_length , self.projection_features)
        y = self.projection_layer(y)

        x_position, (final_hidden_position, final_cell_position) = self.position_rnn(  y , (position_new_hidden, position_new_cell) )
        x_rotation, (final_hidden_rotation, final_cell_rotation) = self.rotation_rnn(  y , (rotation_new_hidden, rotation_new_cell) )
       # print(x_position.shape)
        position_predictions1 = self.position_prediction_layer1(x_position)
        position_predictions1 = self.tanh(position_predictions1)
        position_predictions2 = self.position_prediction_layer2(position_predictions1)
        position_predictions2 = self.tanh(position_predictions2)
        position_predictions = self.position_prediction_layer3(position_predictions2)


        rotation_predictions1 = self.rotation_prediction_layer1(x_rotation)
        rotation_predictions1 = self.tanh(rotation_predictions1)
        rotation_predictions2 = self.rotation_prediction_layer2(rotation_predictions1)
        rotation_predictions2 = self.tanh(rotation_predictions2)
        rotation_predictions = self.rotation_prediction_layer3(rotation_predictions2)
        rotation_norms = torch.norm(rotation_predictions,dim=2)
        rotation_norms = torch.clamp(rotation_norms, 1E-4, 1E20)
        rotation_predictions = rotation_predictions/rotation_norms[:,:,None]

        return position_predictions, rotation_predictions