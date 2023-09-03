from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#windows和linux设置字体的方式
# font = {'family' : 'Microsoft YaHei',
#         'weight':'bold',
#         'size':'larger'}
# matplotlib.rc("font",**font)
# matplotlib.rc("font",**font)

#另外一种设置字体的方式
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

# # 设置图片大小
# fig = plt.figure(figsize=(20,8),dpi=80) #figsize表长宽
# x = range(2,26,2)
# y = [15,13,14.5,17,20,25,26,26,27,22,18,15]
# plt.plot(x,y)
# # 设置数轴的刻度
# plt.xticks(x)
# plt.yticks(range(min(y),max(y)+1))
# # 保存
# #plt.savefig("./t1.png")
# plt.show()

# x = range(120)
# a = [random.randint(20,35) for i in range(120)]
# plt.figure(figsize=(20,8),dpi=80)
# plt.plot(x,a)
#
# #调整x轴的刻度
# _xtick_labels = ["10点{}分".format(i) for i in range(60)]
# _xtick_labels += ["11点{}分".format(i) for i in range(60)]
#
# #取步长，数字和字符串一一对应，数据的长度一样
# plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)     #rotation表示旋转的度数
#
# #添加描述信息
# plt.xlabel("时间",fontproperties=my_font)
# plt.ylabel("温度 单位（℃）",fontproperties=my_font)
# plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)
#
# plt.show()


a = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x = range(11,31)
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,a,label="自己",color="r",linestyle="--",linewidth=2,alpha=0.5)
plt.plot(x,b,label = "同桌")
x_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,x_labels,fontproperties=my_font)
plt.yticks(range(9))

#绘制网格
plt.grid(alpha = 0.3,linestyle="--")      #alpha调整网格透明度

#添加图例
plt.legend(prop=my_font,loc="upper left")    #prop用来显示中文

plt.xlabel("岁数",fontproperties=my_font)
plt.ylabel("个数",fontproperties=my_font)
plt.title("每年交女朋友的数量走势",fontproperties=my_font)
plt.show()