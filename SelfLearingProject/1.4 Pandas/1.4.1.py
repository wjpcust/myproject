'''
---------------pandas常用数据类型----------------

1.Series 一维，带标签数组
2.DataFrame 二维，Series容器


--------------pandas之Series切片和索引------------

切片： 直接传入start、end或者步长即可
索引： 一个的时候直接传入序号或者index，多个的时候传入序号或者index的列表
'''
import pandas as pd

t = pd.Series([1,2,31,14,2],index=list("abcde"))    #index表示索引
print(t)

#通过字典创建一个Series，注意其中的索引就是字典的键
temp_dict = {"name":"xiaohong","age":30,"tel":10086}
t1 = pd.Series(temp_dict)
print(t1)