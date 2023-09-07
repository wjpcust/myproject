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

writer.close()