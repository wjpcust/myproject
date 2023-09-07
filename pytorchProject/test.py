import torch
import torchvision
from PIL import Image
from torch import nn

image_path = './imgs/airplane.png'
image = Image.open(image_path)
print(image)

image = image.convert('RGB')        #png格式是四通道，除了RGB三通道外，还有一个透明度通道，调用image.convert保留其颜色通道

transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32,32)),
                                            torchvision.transforms.ToTensor()])

image = transform(image)
print(image)

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

model = torch.load('tudui_9.pth')
print(model)

image = torch.reshape(image,(1,3,32,32))

# 因为模型使用GPU进行训练的，所以要用cuda指定设备为GPU
image = image.cuda()
model.eval()        #把模型转化为测试类型
with torch.no_grad():
    output = model(image.cuda())
print(output)

print(output.argmax(1))