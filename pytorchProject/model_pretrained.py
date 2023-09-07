import torchvision
from torch import nn

# train_data = torchvision.datasets.ImageNet("./data_image_net",split='train',download=True,transform=torchvision.transforms.ToTensor())

vgg16_false = torchvision.models.vgg16(pretrained=False)
vgg16_true = torchvision.models.vgg16(pretrained=True)

print(vgg16_true)

train_data = torchvision.datasets.CIFAR10('./dataset',train=True,transform=torchvision.transforms.ToTensor(),download=True)

vgg16_true.classifier.add_module('add_linear',nn.Linear(1000,10))       #原输出1000个分类，通过在classifier中添加一层线性改为输出10个分类
print(vgg16_true)

print(vgg16_false)
vgg16_false.classifier[6] = nn.Linear(4096,10)      #将原来的输出1000，改为10
print(vgg16_false)