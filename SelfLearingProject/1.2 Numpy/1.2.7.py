"""
1.数组的拼接
np.vstack((t1,t2))  -->  竖直拼接
np.hstack((t1,t2))  -->  水平拼接

2.数组的行列交换
t[[1,2],:] = t[[2,1],:]  -->  行交换
t[:,[0,2]] = t[:,[2,0]]  -->  列交换


--------------numpy更多好用的方法------------------

1.获得最大值最小值的位置
    np.argmax(t.axis=0)
    np.argmin(t.axis=1)
2.创建一个全为0的数组：np.zeros((3,4))
3.创建一个全为1的数组：np.ones((3,4))
4.创建一个对角线为1的正方形数组（方阵）：np.eye(3)


---------------numpy生成随机数---------------------

.rand(d0,d1,..,dn)            ：创建d0-dn维度的均匀分布的随机数数组，浮点数，范围从0-1
.randn(d0,d1,..,dn)           ：创建d0-dn维度的标准正态分布随机数，浮点数，平均数0，标准差1
.randint(low,high,(shape))    ：从给定上下范围选取随机数整数，范围是low-high，形状是shape
.uniform(low,high,(size))     ：产生具有均匀分布的数组，low起始值，high结束值，size形状
.normal(loc,scale,(size))     ：从指定正态分布中随机抽取样本，分布中心是loc（概率分布的均值），标准差是scale，形状是size
.seed(s)                      ：随机数种子，s是给定的种子值。因为计算机生成的是伪随机数，所以通过设定相同的随机数种子，可以每次生成相同的随机数


---------------numpy的注意点copy和view-----------------

1.a=b完全不复制，a和b相互影响
2.a=b[:]，视图的操作，一种切片，会创建新的对象a，但是a的数据完全由b保管，他们两个的数据变化是一致的
3.a=b.copy()，复制，a和b互不影响

"""
from matplotlib import pyplot as plt
from matplotlib import font_manager
import numpy as np

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

#确定文件路径
us_file_path = "E:/US_video_data.csv"
uk_file_path = "E:/GB_video_data.csv"

#获得文件内容
us_file = np.loadtxt(us_file_path,delimiter=',',dtype=int)
uk_file = np.loadtxt(uk_file_path,delimiter=',',dtype=int)

#添加国家信息
#构造全为0的数据
zeros_data = np.zeros((us_file.shape[0],1)).astype(int)     #参数表示生成：us_file.shape[0]行，1列的数据
#构造全为1的数据
one_data = np.ones((uk_file.shape[0],1)).astype(int)

us_file = np.hstack((us_file,zeros_data))
uk_file = np.hstack((uk_file,one_data))

#数据竖直合并
union_file = np.vstack((us_file,uk_file))

plt.figure(figsize=(20,8),dpi=80)

x_like = union_file[:,1]
y_comment = union_file[:,-2]

plt.scatter(x_like,y_comment)

plt.show()