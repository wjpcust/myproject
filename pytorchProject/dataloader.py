import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

#准备的测试数据集
test_data = torchvision.datasets.CIFAR10("./dataset",train=False,transform=torchvision.transforms.ToTensor())

test_loader = DataLoader(dataset=test_data,batch_size=64,shuffle=True,num_workers=0,drop_last=False)     #batch_size表示每次从test_data中取64个数据集并进行打包

#测试数据集中第一张图片及target
img,target = test_data[0]
print(img.shape)
print(target)

writer = SummaryWriter("dataloader")
step = 0
for data in test_loader:
    imgs,targets = data
    # print(imgs.shape)
    # print(targets)
    writer.add_images("test_data1",imgs,step)
    step += 1
0
writer.close()