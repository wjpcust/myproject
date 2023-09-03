"""
---------------------PeriodIndex-------------------
DatetimeIndex:时间戳
PeriodIndex:时间段

period = pd.PeriodIndex(year=data["year"],month=data["month"],day=data["day"],hour=data["hour"],freq="H")

如果要给这个时间段降采样：
    data = df.set_index(period).resample("10D").mean()
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option("display.max_columns",None)

file_path = "E:/Datasets/PM2.5/BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

#把分开的时间字符串通过PeriodIndex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df['year'],month=df['month'],day=df['day'],hour=df['hour'],freq="H")
df['datetime'] = period

#把datetime设置为索引
df.set_index("datetime",inplace=True)

#进行降采样
# df = df.resample("M").mean()

#处理缺失数据，删除缺失数据
data = df["PM_US Post"].dropna()

_x = data.index
_y = data.values

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)
3.11
plt.xticks(range(0,len(_x),20),list(_x)[::20])

plt.show()