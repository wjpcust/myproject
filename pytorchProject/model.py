from torch import nn
import torch

# 搭建网络模型
class Tudui(nn.Module):
    def __init__(self):
        # 父类初始化
        super(Tudui, self).__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 32, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(64 * 4 * 4, 64),
            nn.Linear(64, 10)
        )

    def forward(self, x):
        x = self.model(x)
        return x

# 检查搭建网络的正确性
if __name__ == '__main__':
    tudui = Tudui()
    input = torch.ones((64,3,32,32))        # batchsize=64 , kernel=3 , line=1 , row=1
    output = tudui(input)
    print(output.shape)