#Resize的使用
#Normalize的使用
#ToTensor的用法
from PIL import Image
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter("logs")
img = Image.open("E:\\pytorchProject\\data\\train\\bees_image\\132511197_0b86ad0fff.jpg")

# ToTensor
tran_tensor = transforms.ToTensor()
img_tensor = tran_tensor(img)
writer.add_image("ToTensorTest",img_tensor)

# Normalize
# 归一化公式：output[channel] = (input[channel] - mean[channel]) / std[channel]
print(img_tensor[0][0][0])
# (input-0.5)/0.5 = 2*input-1
trans_norm = transforms.Normalize([6,3,2],[9,3,5])
img_norm = trans_norm(img_tensor)
print(img_norm[0][0][0])
writer.add_image("Normalize",img_norm,2)

# Resize
print(img.size)
trans_resize = transforms.Resize((512,512))
# img PIL -> resize -> img_resize PIL
img_resize = trans_resize(img)
# img_resize PIL -> totensor -> img_resize tensor
img_resize = tran_tensor(img_resize)
print(img_resize)
writer.add_image("Resize",img_resize,0)

# Compose - resize - 2
'''
----------------Compose用法---------------------

Compose()中的参数需要一个列表，数据需要是transforms类型
Compose([tranforms参数1,tranforms参数2,...])
'''
trans_resize_2 = transforms.Resize(512)
# PIL -> PIL -> tensor
trans_compose = transforms.Compose([trans_resize_2,tran_tensor])
img_resize_2 = trans_compose(img)
writer.add_image("Resize",img_resize_2,1)

# RandonCrop
trans_random = transforms.RandomCrop((356,456))
trans_compose_2 = transforms.Compose([trans_random,tran_tensor])
for i in range(10):
    img_crop = trans_compose_2(img)
    writer.add_image("RandomHW",img_crop,i)

writer.close()