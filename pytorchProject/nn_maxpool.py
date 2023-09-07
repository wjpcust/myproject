import torch
import torchvision
from torch import nn
from torch.nn import MaxPool2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

dataset = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor(),download=True)

dataloader = DataLoader(dataset,batch_size=64)

# input = torch.tensor([[1,2,0,3,1],
#                       [0,1,2,3,1],
#                       [1,2,1,0,0],
#                       [5,2,3,1,1],
#                       [2,1,0,1,1]],dtype=torch.float32)     #不改变数据类型，则无法对long数据进行实现
#
# input = torch.reshape(input,(-1,1,5,5))     #-1  -->  自己计算batchsize
#
# print(input.shape)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui,self).__init__()
        self.maxpool1 = MaxPool2d(kernel_size=3,ceil_mode=True)     #ceil_mode为True时，向上取整

    def forward(self,input):
        output = self.maxpool1(input)
        return output

tudui = Tudui()

writer = SummaryWriter("maxpool_logs")

step = 0

for data in dataloader:
    imgs,targets = data
    writer.add_images("input",imgs,step)
    output = tudui(imgs)
    #池化不改变维度，即不改变通道数，不用进行reshape
    writer.add_images("output",output,step)
    step += 1

writer.close()
