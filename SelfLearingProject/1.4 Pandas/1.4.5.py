import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv("E:/Datasets/IMDB-Movie-Data.csv")

#统计分类列表
temp_list = df["Genre"].str.split(",").tolist()

genre_list = list(set([i for j in temp_list for i in j]))

#构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)

#给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    #zero_df.loc[0,["Sci-fi","Musical"]] = 1
    zero_df.loc[i,temp_list[i]] = 1

#统计每个分类的电影的数量和
genre_count = zero_df.sum(axis=0)

#排序
genre_count = genre_count.sort_values(ascending=False)
_x = genre_count.index
_y = genre_count.values

plt.figure(figsize=(20,8),dpi=80)

plt.bar(_x,_y)

plt.show()