'''
----------------数据合并之join----------------

join：默认情况下是把行索引相同的数据合并到一起
t1.join(t2)

---------------数据合并之merge----------------

merge：按照指定的列把数据按照一定的方式合并到一起
df1.merge(df2,on="x",how="inner")
inner:交集
outer:并集，NaN补全
left:左边为准，NaN补全
right:右边为准，NaN补全
'''