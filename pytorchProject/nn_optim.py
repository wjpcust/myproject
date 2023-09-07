import torch
import torchvision
from torch import nn
from torch.nn import Conv2d,MaxPool2d,Flatten,Linear,CrossEntropyLoss,Sequential
from torch.utils.data import DataLoader

dataset = torchvision.datasets.CIFAR10('./dataset',train=False,transform=torchvision.transforms.ToTensor(),download=True)
dataloader = DataLoader(dataset,1)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui,self).__init__()
        self.model1 = Sequential(
            Conv2d(3,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,32,5,padding=2),
            MaxPool2d(2),
            Conv2d(32,64,5,padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024,64),
            Linear(64,10)
        )

    def forward(self,x):
        x = self.model1(x)
        return x

loss = CrossEntropyLoss()
tudui = Tudui()
optim = torch.optim.SGD(tudui.parameters(),lr=0.01)       #随机梯度下降
#lr --> 学习速率
for epoch in range(20):     #对数据进行多轮学习
    running_loss = 0.0
    for data in dataloader:
        imgs,targets = data
        outputs = tudui(imgs)
        result_loss = loss(outputs,targets)
        optim.zero_grad()       #把网络模型当中每一个可以调节的参数对应的梯度调为0
        result_loss.backward()      #反响传播，求出每一个节点对应的梯度
        optim.step()        #对每个参数进行调优
        running_loss = running_loss + result_loss       #整体误差总和
    print(running_loss)