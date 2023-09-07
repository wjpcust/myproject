import torch
import torchvision.models
from torch import nn
from model_save import *

#加载方式一 --> 保存方式一
# model = torch.load('vgg16_method1.pth')
# print(model)

#加载方式二 --> 保存方式二
vgg16 = torchvision.models.vgg16(pretrained=False)
vgg16.load_state_dict(torch.load('vgg16_method2.pth'))
# model = torch.load('vgg16_method2.pth')
# print(vgg16)

#陷阱
#将之前的网络结构定义给出
# class Tudui(nn.Module):
#     def __init__(self):
#         super(Tudui,self).__init__()
#         self.conv1 = nn.Conv2d(3,64,kernel_size=3)
#
#     def forward(self,x):
#         x = self.conv1(x)
#         return x

model = torch.load('tudui_method1.pth')
print(model)