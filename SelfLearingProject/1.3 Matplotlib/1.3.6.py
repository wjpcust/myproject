from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

# a = []
# for i in range(1,251):
#     a.append(random.randint(78,159))
#
# plt.figure(figsize=(20,8),dpi=80)
#
# #计算组数
# d = 3   #组距
# num_bins = (max(a)-min(a))//d
#
# plt.hist(a,num_bins,density=True)
#
# plt.xticks(range(min(a),max(a)+d,d))
# plt.grid(alpha=0.5,linestyle="--")
#
# plt.show()

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]

plt.figure(figsize=(20,8),dpi=80)

plt.bar(range(len(quantity)),quantity,width=1)

_x = [i-0.5 for i in range(13)]
_xtick_labels = interval+[150]
plt.xticks(_x,_xtick_labels)

plt.grid(alpha=0.5)

plt.show()