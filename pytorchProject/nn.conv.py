import torch
import torch.nn.functional as F

#输入图像
input = torch.tensor([[1,2,0,3,1],
                      [0,1,2,3,1],
                      [1,2,1,0,0],
                      [5,2,3,1,1],
                      [2,1,0,1,1]])

#卷积核
kernel = torch.tensor([[1,2,1],
                       [0,1,0],
                       [2,1,0]])

#尺寸变换
input = torch.reshape(input,(1,1,5,5))      #1batchsize，1通道，1高度，1宽度
kernel = torch.reshape(kernel,(1,1,3,3))

print(input.shape)
print(kernel.shape)

output = F.conv2d(input,kernel,stride=1)
print(output)

output2 = F.conv2d(input,kernel,stride=2)
print(output2)

output3 = F.conv2d(input,kernel,stride=1,padding=1)
print(output3)