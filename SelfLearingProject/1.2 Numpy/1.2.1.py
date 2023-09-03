import numpy as np
import random

#使用numpy生成数组，得到ndarray类型
t1 = np.array([1,2,3])
t2 = np.array(range(10))
t3 = np.arange(10)
t4 = np.array(range(1,4),dtype=float)
t5 = np.array([1,1,0,1,0],dtype=bool)
t6 = t5.astype("int8")  #更改数据类型
t7 = np.array([random.random() for i in range(10)])
t8 = np.round(t7,2)     #保留2位小数
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
print(t7)
print(t8)