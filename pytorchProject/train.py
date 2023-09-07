# 完整的模型训练套路

import torch
from torch import nn
import torchvision
from torch.utils.data import DataLoader
from model import *
from torch.utils.tensorboard import SummaryWriter
import time

# 准备数据集
train_data = torchvision.datasets.CIFAR10(root='./dataset',train=True,transform=torchvision.transforms.ToTensor(),download=True)

test_data = torchvision.datasets.CIFAR10(root='./dataset',train=False,transform=torchvision.transforms.ToTensor(),download=True)

# 查看数据集中的图片数量
train_data_size = len(train_data)
test_data_size = len(test_data)
print("训练数据集的长度为：{}".format(train_data_size))
print("测试数据集的长度为：{}".format(test_data_size))

# 利用 DataLoader 来加载数据集
train_dataloader = DataLoader(train_data,batch_size=64)
test_dataloader = DataLoader(test_data,batch_size=64)

# 创建网络模型
tudui = Tudui()

# 创建损失函数
loss_fn = nn.CrossEntropyLoss()     #交叉熵

# 创建优化器
# learning_rate = 0.01        #学习速率
# 1e-2 = 1 x (10)^(-2) = 1 / 100 =0.01
learning_rate = 1e-2
optimizer = torch.optim.SGD(tudui.parameters(),lr=learning_rate)       #随机梯度下降

# 设置训练网络的一些参数
# 记录训练的次数
total_train_step = 0
# 记录测试的次数
total_test_step = 0
# 训练的轮数
epoch = 10

# 添加tensorboard
writer = SummaryWriter('train_logs')

start_time = time.time()

for i in range(epoch):
    print("--------------第{}轮训练开始-------------".format(i+1))

    # 训练步骤开始
    for data in train_dataloader:
        imgs,targets = data
        outputs = tudui(imgs)
        loss = loss_fn(outputs,targets)

        # 优化器优化模型
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step += 1
        if total_train_step % 100 ==0:
            end_time = time.time()
            print("训练次数：{},Loss:{}".format(total_train_step,loss))
            print(end_time-start_time)
            writer.add_scalar('train_loss',loss.item(),total_test_step)

    # 测试步骤开始
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs,targets = data
            outputs = tudui(imgs)
            loss = loss_fn(outputs,targets)
            total_test_loss += loss.item()
            accuracy = (outputs.argmax(1) == targets).sum()      #每次正确个数求和
            total_accuracy += accuracy

    print("整体测试集上的Loss:{}".format(total_test_loss))
    print("整体测试集上的正确率:{}".format(total_accuracy/test_data_size))
    writer.add_scalar('test_loss',total_test_loss,total_test_step)
    writer.add_scalar('test_accuracy',total_accuracy/test_data_size,total_test_step)
    total_test_step += 1

    torch.save(tudui,"tudui_{}.pth".format(i))
    print("模型已保存")

writer.close()