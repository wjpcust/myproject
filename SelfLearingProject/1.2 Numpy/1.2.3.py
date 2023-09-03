import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_fonts = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

us_file_path = "E:/US_video_data.csv"
uk_file_path = "E:/GB_video_data.csv"

t_us = np.loadtxt(us_file_path,delimiter=',',dtype='int') #读取本地文件
t_uk = np.loadtxt(uk_file_path,delimiter=',',dtype='int')
'''
delimiter:制定边界符是什么，不指定会导致每行数据为一个整体的字符串而报错
dtype:默认情况下对于较大的数据会将其转变为科学技术的方式
upack:默认是FALSE，为TRUE时相当于转置
'''

# #取行
# print(t2[2])
#
# #取连续多行
# print(t2[2:])
#
# #取不连续多行
# print(t2[[2,8,10]])
#
# #取列
# print(t2[:,0])
#
# #取连续多列
# print(t2[:,2:])
#
# #取不连续多列
# print(t2[:,[0,2]])
#
# #取多个不相邻的点(0,0),(2,1)
# print(t2[[0,2],[0,1]])
# #对数值修改直接取出后再赋值即可
'''
1.numpy的三元运算符：
np.where(t<10,0,10):将t中小于10的值修改为0，大于10的值修改为10

2.numpy中的clip（裁剪）
t.clip(10,18):小于10的替换为10，大于18的替换为18

3.numpy中的nan和inf（浮点类型）
nan(NAN,Nan):not a number 表示不是一个数字
inf(-inf,inf):infinity,inf表示正无穷，-inf表示负无穷
注意：
    a. 两个nan是不相等的
    b. np.nan!=np.nan
    c. 利用以上特性可以判断数组中nan的个数
        np.count_nonzero(t!=t1)
    d. 通过np.isnan(a)来判断一个数字是否为nan，返回bool类型，比如希望把nan替换为0：t[np.isnan(t)]=0
    e. nan和任何值计算都为nan
'''

"""
numpy中常用统计函数
求和：t.sum(axis=None)
均值：t.mean(a,axis=None)
中值：np.median(t,axis=None)
最大值：t.max(axis=None)
最小值：t.min(axis=None)
极值：np.ptp(t,axis=None)即最大值和最小值之差
标准差：t.std(axis=None)

默认返回多维数组的全部的统计结果，如果指定axis则返回一个当前轴上的结果
"""

plt.figure(figsize=(20,8),dpi=80)

#取评论的数据
t_us_comments = t_us[:,-1]
t_uk_comments = t_uk[:,-1]

#选择比5000小的数据
t_us_comments = t_us_comments[t_us_comments<=5000]

#取组数
d = 50

bin_nums_us = (t_us_comments.max()-t_us_comments.min())//d
bin_nums_uk = (t_uk_comments.max()-t_uk_comments.min())//d

plt.hist(t_us_comments,bin_nums_us)

plt.show()
