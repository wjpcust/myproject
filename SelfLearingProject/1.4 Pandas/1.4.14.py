import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

file_path = "E:/Datasets/911.csv"
plt.figure(figsize=(20,8),dpi=80)
pd.set_option("display.max_columns",None)

df = pd.read_csv(file_path)

df["timeStamp"] = pd.to_datetime(df["timeStamp"])

df.set_index("timeStamp",inplace=True)

# print(df.head(5))

#统计911数据中不同月份电话次数

count_by_month = df.resample("M").count()['title']
# print(count_by_month)

_x = count_by_month.index
_y = count_by_month.values
_x = [i.strftime("%Y-%m-%d") for i in _x]
plt.plot(range(len(_x)),_y)

plt.xticks(list(range(len(_x))),_x,rotation=45)

plt.show()