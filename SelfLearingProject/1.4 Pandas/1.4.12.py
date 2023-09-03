
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

file_path = "E:/Datasets/911.csv"
plt.figure(figsize=(20,8),dpi=80)
pd.set_option("display.max_columns",None)

df = pd.read_csv(file_path)

#获取分类
temp_list = df['title'].str.split(":").tolist()
cate_list = list(set(i[0] for i in temp_list))

#构造全为0的数组
zero = pd.DataFrame(np.zeros((df.shape[0],len(cate_list))),columns=cate_list)

#赋值
for cate in cate_list:
    zero[cate][df['title'].str.contains(cate)] = 1

print(zero.sum(axis=0))