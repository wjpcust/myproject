'''
-----------------分组和聚合-----------------
分组：df.groupby(by="columns_name")

函数名               说明
count               分组中非NA值的数量
sum                 非NA值的和
mean                非NA值的平均值
median              非NA值的算术中位数
std、var             无偏（分母为n-1）标准差和方差
min、max             非NA值的最小值和最大值
'''


import pandas as pd
import numpy as np

file_path="E:/Datasets/directory.csv"

df = pd.read_csv(file_path)

pd.set_option("display.max_columns",None)
# print(df.head(1))
# print(df.info())

grouped = df.groupby(by="Country")
print(grouped)

#DataFrameGroupBy
#可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j)
#     print("*"*100)
#调用聚合方法
country_count = grouped["Brand"].count()     #count()统计数量
print(country_count["US"])
print(country_count["CN"])

#统计中国每个省份店铺数量
china_data = df[df["Country"]=="CN"]
grouped1 = china_data.groupby(by="State/Province").count()["Brand"]
print(grouped1)

#数据按照多个条件进行分组，返回Series
grouped2 = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped2)
print(type(grouped2))

#数据按照多个条件进行分组，返回DataFrame
grouped3 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
print(grouped3)
print(type(grouped3))