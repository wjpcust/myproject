from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
import cv2

#用法
'''
-------------------tensor数据类型-------------------
通过transforms.ToTensor去看两个问题
1、transforms该如何使用（python）
2、为什么需要Tensor数据类型
'''

img_path = "data/train/bees_image/29494643_e3410f0d37.jpg"
img = Image.open(img_path)

writer = SummaryWriter("logs")

#1、transforms该如何使用（python）

#ToTensor的使用
#将PIL Image 或者 numpy.ndarray 数据转化为Tensor型数据
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)

writer.add_image("Tensor_img",tensor_img)

writer.close()

