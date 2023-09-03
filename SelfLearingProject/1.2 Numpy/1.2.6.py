import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_fonts = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

uk_file_path = "E:/GB_video_data.csv"

t_uk = np.loadtxt(uk_file_path,delimiter=',',dtype='int')

#选择喜欢数比500000小的数据
t_uk = t_uk[t_uk[:,1]<=800000]

t_uk_comments = t_uk[:,-1]
t_uk_like = t_uk[:,1]

plt.figure(figsize=(20,8),dpi=80)

plt.scatter(t_uk_like,t_uk_comments)

plt.show()