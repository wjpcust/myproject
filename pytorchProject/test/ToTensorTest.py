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
writer.close()