'''
-----------------常见的Transforms-------------------
PIL     -->     Image.open()
tensor  -->     ToTensor()
narrays -->     cv.imread()
'''
from PIL import Image
from torchvision import transforms

img = Image.open("data/train/bees_image/39672681_1302d204d1.jpg")
print(img)