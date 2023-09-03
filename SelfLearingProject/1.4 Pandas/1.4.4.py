import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("E:/Datasets/IMDB-Movie-Data.csv")

print(df.info())

#获取平均评分
print(df["Rating"].mean())

#获取导演的人数
print(len(set(df["Director"].tolist())))        #set创建无序不重复数据集合
print(len(df["Director"].unique()))             #unique生成不重复列表

#获取演员人数
# print(df["Actors"])
temp_actors_list = df["Actors"].str.split(",").tolist()
# print(temp_actors_list)
actors_list = [i for j in temp_actors_list for i in j]
# print(actors_list)
actors_num = len(set(actors_list))
print(actors_num)

#rating,runtime分布情况
#选择图形，直方图
#准备数据
runtime_data = df["Runtime (Minutes)"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

#计算组数
num_bin = (max_runtime-min_runtime)//5

plt.figure(figsize=(20,8),dpi=80)

plt.hist(runtime_data,num_bin)

plt.xticks(range(min_runtime,max_runtime+5,5))

plt.show()