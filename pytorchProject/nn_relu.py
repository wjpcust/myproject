import torch
from torch import nn
from torch.nn import ReLU
from torch.nn import Sigmoid
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

#relu -->  小于0为0，大于0为本身
# input = torch.tensor([[1,-0.5],
#                       [-1,3]])
#
# input = torch.reshape(input,(-1,1,2,2))     #-1代表自己算batchsize

dataset = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor(),download=True)

dataloader = DataLoader(dataset,batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui,self).__init__()
        self.relu = ReLU()
        self.sigmoid = Sigmoid()

    def forward(self,input):
        output = self.sigmoid(input)
        return output

tudui = Tudui()
# output = tudui(input)
# print(output)
step = 0

writer = SummaryWriter("sigmoid_logs")

for data in dataloader:
    imgs,targets = data
    writer.add_images("input",imgs,step)
    output = tudui(imgs)
    writer.add_images("output",output,step)
    step += 1

writer.close()