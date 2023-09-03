'''
------------------pandas之DataFrame------------------

DataFrame对象既有行索引，又有列索引
行索引，表明不同行，横向索引，叫index，0轴，axis=0
列索引，表名不同列，纵向索引，叫columns，1轴，axis=1


------------------DataFrame的基础属性------------------

df.shape        #行数、列数
df.dtypes       #列数据类型
df.ndim         #数据维度
df.index        #行索引
df.columns      #列索引
df.values       #对象值，二维ndarray数组


-------------------DataFrame整体情况查询------------------

df.head(3)      #显示头部几行，默认5行
df.tail(3)      #显示末尾几行，默认5行
df.info()       #相关信息概览：行数，列数，列索引，列非空值个数，列类型，内存占用
df.describe()   #快速合计统计结果：计数，均值，标准差，最大值，四分位数，最小值


-------------------DataFrame排序方法-----------------------

df.sort_values(by="Count_AnimalName",ascending=False)      #ascending为True时为升序，为False时为降序


-------------------pandas之loc----------------------------

df.loc  通过标签索引行数据
df.iloc 通过位置获取行数据


---------------------pandas之布尔索引-------------------------

df[df["Count_AnimalName"]>800]
df[(df["Count_AnimalName"]>800)&(df["Count_AnimalName"]<1000)]      #不同条件之间需要用括号括起来


-----------------------缺失数据的处理--------------------------


数据缺失通常有两种情况：
    一种就是空，None等，在pandas是NaN（和np.nan一样）
    另外一种是我们让其为0

判断数据是否为NaN：pd.isnull(df),pd.notnull(df)
处理方式1：删除NaN所在行列 dropna(axis=0,how='any,inplace=False)    #how中参数为any:只要有nan就删    all:全为nan时删
                                                                #inplace表示是否修改原来的数据
处理方式2：填充数据，t.fillna(t.mean()),t.fillna(t.median()),t.fillna(0)

处理为0的数据：t[t==0]=np.nan
并不是每次为0的数据都需要处理
计算平均值等情况，nan是不参与计算的，但是0会
'''
import pandas as pd
import numpy as np

# t1 = pd.DataFrame(np.arange(12).reshape(3,4))
# t2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))    #指定行列索引
# print(t1)
# print(t2)
#
# #字典
# d1 = {"name":["xuhua","xiaoguang"],"age":[18,22],"tel":[10086,10010]}
# t3 = pd.DataFrame(d1)
# print(t3)
#
# #列表
# d2 = [{"name":"xiaowang","age":22},{"name":"xaioguang","tel":10086},{"name":"xiaoxing","age":23}]
# t4 = pd.DataFrame(d2)
# print(t4)

# df = pd.read_csv("E:/Datasets/dogNames2.csv")
# # print(df.head())
# # print(df.info())
#
# #dataframe中排序的方法
# df = df.sort_values(by="Count_AnimalName",ascending=False)      #ascending为True时为升序，为False时为降序
#
# #pandas取行或者列的注意点
# # - 方括号写数组，表示取行，对行进行操作
# # - 写字符串，表示取列索引，对列进行操作
# print(df[:20])
# print(df[:20]["Row_Labels"])

t2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
print(t2.loc["a","z"])
print(t2.loc["a"])
print(t2.loc[:,"y"])
print(t2.loc[["a","c"]])
print(t2.loc[:,["w","z"]])
print(t2.loc[["a","b"],["w","z"]])
print(t2.loc["a":"c",["w","z"]])

print("*"*100)

print(t2.iloc[1,:])
print(t2.iloc[:,2])
print(t2.iloc[:,[2,1]])
print(t2.iloc[[0,2],[2,1]])
print(t2.iloc[1:,:2])