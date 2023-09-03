import numpy as np
a = np.array([[3,4,5,6,7,8],[4,5,6,7,8,9]])
print(a)

#查看数组形状
print(a.shape)

#修改数组形状(不改变原数组形状)
print(a.reshape((3,4)))
print(a.shape)

print(np.arange(24).reshape((2,3,4)))

#输出一维数组
print(a.flatten())