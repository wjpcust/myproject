'''
------------------索引和复合索引--------------------

简单的索引操作：
    获取index：df.index
    指定index：df.index = ['x','y']
    重新设置index：df.reindex(list("abcdef"))
    指定某一列作为index：df.set_index("Country",drop=False)         #drop默认为True，表示删掉原有的Country列，若想保留，则置drop为False
    返回index的唯一值：df.set_index("Country").index.unique()
'''
import pandas as pd
import numpy as np

# df1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('ABC'),columns=list('abcd'))
# print(df1)
#
# #指定索引
# df1.index = list('abc')
# print(df1)
#
# #重新设置索引
# print(df1.reindex(list('abcd')))
#
# #指定某一列作为索引
# print(df1.set_index("a",drop=False))        #drop
#
# #设置多个索引
# print(df1.set_index(['a','b']))
# print(df1.set_index(['a','b']).index)

a = pd.DataFrame({'a':range(7),'b':range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':list('hjklmno')})

print(a)

b = a.set_index(['c','d'])

print(b)

c = b['a']

#注意：此时c的类型为Series
print(c)
print(type(c))
print(c['one']['j'])
print(c['one'])

d = a.set_index(['d','c'])['a']
print(d)

#取one对应的数据，用swaplevel()取里层索引
print(d.swaplevel()['one'])

#对DataFrame类型取索引
print(b.loc['one'].loc['h'])
print(b.swaplevel().loc['h'])