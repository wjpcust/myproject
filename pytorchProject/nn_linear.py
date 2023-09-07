import torch
import torchvision
from torch import nn
from torch.nn import Linear
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor(),download=True)

dataloader = DataLoader(dataset,batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui,self).__init__()
        self.linear = Linear(196608,10)

    def forward(self,input):
        output = self.linear(input)
        return output

tudui = Tudui()


for data in dataloader:
    imgs,targets = data
    print(imgs.shape)
    output = torch.flatten(imgs)        #将原始数据展为1行
    print(output.shape)
    output = tudui(output)
    print(output.shape)