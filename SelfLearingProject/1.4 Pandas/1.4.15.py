import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

file_path = "E:/Datasets/911.csv"
plt.figure(figsize=(20,8),dpi=80)
pd.set_option("display.max_columns",None)

df = pd.read_csv(file_path)

#把时间字符串转化为时间类型设置为索引
df["timeStamp"] = pd.to_datetime(df["timeStamp"])

#添加列，表示分类
temp_list = df['title'].str.split(':').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)))

df.set_index("timeStamp",inplace=True)

#分组
for group_name,group_data in df.groupby(by="cate"):

    count_by_month = group_data.resample("M").count()['title']

    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y-%m-%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)),_x,rotation=45)
plt.legend(loc="best")
plt.show()