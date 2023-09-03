'''
----------------------pandas中的时间序列---------------------

1.生成一段时间范围
pd.date_range(start=None,end=None,periods=None,frea='D')

start和end以及freq配合能够生成start和end范围内以频率freq的一组时间索引
start和periods以及freq配合能够生成从start开始的频率为freq的periods个时间索引
freq中D代表天，10D则以十天的频率生成时间索引（M代表月）

2.把时间字符串转化为时间序列
df["timeStamp"] = pd.to_datetime(df["timeStamp"],format="")

format参数大多情况下可以不写，但是对于pandas无法格式化的时间字符串，可以使用该参数，比如包含中文


-------------------------pandas重采样-------------------------

重采样：指的是将时间序列从一个频率转化为另一个频率进行处理的过程
降采样：高频率数据转化为低频率数据
升采样：低频率数据转化为高频率数据

resample方法实现频率转化：
    t.resample("M")             将原数据频率转化为“月”
    t.resample("10D")           将原数据频率转化为”十天“

'''
import pandas as pd

datetime = pd.date_range(start="20171230",end="20180131",freq="D")
print(datetime)

datetime = pd.date_range(start="20171230",periods=20,freq="D")
print(datetime)