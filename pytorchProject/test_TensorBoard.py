from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image

writer = SummaryWriter("logs")
img_path = "data/train/ants_image/5650366_e22b7e1065.jpg"
img_PIL = Image.open(img_path)
img_array = np.array(img_PIL)

writer.add_image("test",img_array,2,dataformats='HWC')
#1代表step，步骤
#HWC代表：高度、宽度、通道数
for i in range(100):
    writer.add_scalar("y=2x",2*i,i)     #参数1：标题     参数2：y轴      参数3:x轴

writer.close()