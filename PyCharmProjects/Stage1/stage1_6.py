#数据容器入门
"""
python数据容器：
list(列表)、tuple(元组)、str(字符串)、set(集合)、dict(字典)
"""


#列表的定义语法
"""
基本语法：
# 字面量
[元素1,元素2,元素3,元素4,...]

# 定义变量
变量名称 = [元素1,元素2,元素3,元素4,...]

# 定义空列表
变量名称 = []
变量名称 = list()
"""

"""
namelist = ['itheima','ittest','python']
print(namelist)
print(type(namelist))

mylist = ['itheima',666,True]
print(mylist)
print(type(mylist))

#嵌套列表
my_list = [[1,2,3],[4,5,6],[7,8]]
print(my_list)
print(type(my_list))
"""


#列表的下标索引，通过索隐取数据，一定不要超过范围
"""
name_list = ['Tom','Lily','Rose']
print(name_list[0])
print(name_list[1])
print(name_list[2])
#反向索引
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
#嵌套列表的下标
my_list = [[0,1,2],[3,4,5],[6,7]]
print(my_list[0][2])
print(my_list[1][0])
print(my_list[2][1])
"""


#列表的常用操作方法
"""
1.查找某元素的下标
功能：查找指定元素在列表的下标，如果找不到，报错ValueError
语法：列表.index(元素)

2.修改特定位置的元素值
语法：列表[下标] = 值

3.插入元素
功能：在指定的下标位置，插入指定的元素
语法：列表.insert(下标,元素)

4.追加元素
功能：将指定元素，追加到列表的尾部
语法：列表.append(元素)
扩展功能：将其他数据容器的内容取出，依次追加到列表尾部
语法：列表.extend(其他数据容器)

5.删除元素
语法1：del 列表[下标]
语法2：列表.pop(下标)，可以得到被删元素
删除某元素在列表中的第一个匹配项
语法：列表.remove(元素)

6.清空列表内容
语法：列表.clear()

7.统计某元素在列表中的数量
语法：列表.count(元素)

8.统计列表内有多少元素
语法：len(列表)
"""

"""
my_list = ['itheima','ittest','python']
index = my_list.index('itheima')  #查找
print(index)
print(my_list)
my_list[0] = '传智教育'  #修改
print(my_list)
my_list.insert(1,'best')  #插入
print(my_list)
my_list.append('黑马程序员')  #追加
print(my_list)
my_list.extend([4,5,6])  #追加列表
print(my_list)
del my_list[3]  #删除方式一
print(my_list)
element = my_list.pop(1)
print(element)
print(my_list)
my_list.remove('ittest')  #按元素删除
print(my_list)
my_list.clear()  #清空列表
print(my_list)
my_list=[1,2,3,1,1,5,6,4,3]
count = my_list.count(1)  #统计元素数量
print(my_list)
print(count)
print(len(my_list))  #统计列表元素数量
"""

#练习案例：常用功能练习
"""
stu_age_list = [21,25,21,23,22,20]
print(stu_age_list)
stu_age_list.append(31)
print(stu_age_list)
stu_age_list.extend([29,33,30])
print(stu_age_list)
print(stu_age_list[0])
print(stu_age_list[-1])
print(stu_age_list.index(31))
"""


#列表的循环遍历
"""
#while循环
def list_while_func():
    my_list = ["传智教育","黑马程序员","python"]
    index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1
list_while_func()
#for循环
def list_for_func():
    my_list = ["传智教育", "黑马程序员", "python"]
    for element in my_list:
        print(element)
list_for_func()
"""
#练习案例：取出列表中的偶数
"""
mylist = [1,2,3,4,5,6,7,8,9,10]
def while_mylist_func(wl):
    index = 0
    mylist_while = []
    while index < len(wl):
        if int(wl[index]) % 2 == 0:
            mylist_while.append(wl[index])
        index += 1
    print(mylist_while)
while_mylist_func(mylist)

def for_mylist_func(fl):
    mylist_for = []
    for element in fl:
        if int(element) % 2 == 0:
            mylist_for.append(element)
    print(mylist_for)
for_mylist_func(mylist)
"""


#元组的定义和操作
#元组一旦定义完成，就不可修改
"""
# 定义元组字面量
(元素,元素,元素...,元素)
# 定义元组变量
变量名称 = (元素,元素,元素...,元素)
# 定义空元组
变量名称 = ()
变量名称 = tuple()
# 定义单个元素的元组
变量名称 = (元素,)
"""
#元组的相关操作
"""
1.查找某个元素对应的下标
语法：元组.index(元素)

2.统计某个数据在当前元组出现的次数
语法：元组.count(元素)

3.统计元组内元素的个数
语法：len(元组)
"""
#练习案例：元祖的基本操作
"""
mytuple = ('周杰伦',11,['football','music'])
print(mytuple.index(11))
print(mytuple[0])
del mytuple[2][0]
print(mytuple)
mytuple[2].append('coding')
print(mytuple)
"""


#字符串的定义和操作
#同元组一样，是无法修改的数据容器
#字符串的常用操作
"""
1.查找特定字符串的下标索引值
语法：字符串.index(字符串)

2.字符串的替换
语法：字符串.replace(字符串1,字符串2)
功能：将字符串的全部：字符串1，替换为字符串2
注意：不是修改字符串本身，而是得到了一个新字符串

3.字符串的分割
语法：字符串.split(分隔符字符串)
功能：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中
注意：字符串本身不变，而是得到了一个列表对象

4.字符串的规整操作（去前后空格）
语法：字符串.strip()
去前后指定字符串
语法：字符串.strip(字符串)
注意，传入的字符串按单个字符移除，如传入"12"，则"1"和"2"都会移除

5.统计字符串中某字符串出现的次数
语法：字符串.count(字符串)

6.统计字符串长度
语法：len(字符串)
"""
#练习案例：分割字符串
"""
mystr = "itheima itcast boxuegu"
print(mystr.count("it"))
mystr_1 = mystr.replace(" ","|")
print(mystr_1)
mylist = mystr_1.split("|")
print(mylist)
"""


#数据容器的切片
"""
序列支持切片，即：列表、元组、字符串，均支持进行切片操作
切片：从一个序列中，取出一个子序列
语法：序列[起始下标:结束下标:步长]
"""
"""
# 对list进行切片，从1开始，4结束，步长1
mylist = [0,1,2,3,4,5,6]
result1 = mylist[1:4]     #步长默认为1，可以省略不写
print(result1)

# 对tuple进行切片，从头开始，到最后结束，步长1
mytuple = (0,1,2,3,4,5,6)
result2 = mytuple[:]    #起始和结束不写代表从头到尾
print(result2)

# 对str进行切片，从头开始，到最后结束，步长2
mystr="01234567"
result3 = mystr[::2]
print(result3)

# 对str进行切片，从头开始，到最后结束，步长-1
mystr1 = "01234567"
result4 = mystr1[::-1]
print(result4)

# 对列表进行切片，从3开始，到1结束，步长-1
mylist1 = [0,1,2,3,4,5,6]
result5 = mylist1[3:1:-1]
print(result5)

# 对元组进行切片，从头开始，到尾结束，步长-2
mytuple1 = (0,1,2,3,4,5,6)
result6 = mytuple1[::-2]
print(result6)
"""
#练习案例：序列的切片实践
"""
mystr = "万过薪月，员序程马黑来，nohtyP学"
result = mystr[::-1].replace("来","").split("，")
result1 = mystr.split("，")[1].replace("来","")[::-1]
print(result[1])
print(result1)
"""


#集合的定义和操作（不支持重复且内部无序，不支持下标索引访问）
"""
定义基本语法：
# 定义集合字面量
{元素，元素，元素....，元素}
# 定义集合变量
变量名称 = {元素，元素，元素....，元素}
# 定义空集合
变量名称 = set()


常用操作：
1.添加新元素
语法：集合add(元素)。将指定元素，添加到集合内

2.移除元素
语法：集合.remove(元素)。将指定元素，从集合内移除

3.从集合内随机取出元素
语法：集合.pop()
结果：得到一个元素的结果，同时集合本身被修改，元素被移除

4.清空集合
语法：集合.clear()

5.取2个集合的差集
语法：集合1.difference(集合2)
功能：去除集合1和集合2的差集
结果：得到一个新集合，集合1和集合2不变

6.消除2个集合的差集
语法：集合1.difference_update(集合2)
功能：对比集合1和集合2，在集合1内，删除和集合2相同的元素
结果：集合1被修改，集合2不变

7.2个集合合并
语法：集合1.union(集合2)
功能：将集合1和集合2组合成新集合
结果：得到新集合，集合1和集合2不变

8.统计集合元素数量
语法：len(集合)

9.集合的遍历
不支持索引下标，不能用while循环，可以用for循环
"""
"""
my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
print(my_set)
my_set.add("Python")
my_set.add("传智教育")
print(my_set)
my_set.remove("黑马程序员")
print(my_set)
element = my_set.pop()
print(element)
print(my_set)
my_set.clear()
print(my_set)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(set3)
print(set1)
print(set2)
set1.difference_update(set2)
print(set1)
print(set2)
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(set3)
print(set1)
print(set2)
print(len(set3))
for element in set3:
    print(element)
"""
#练习案例：信息去重
"""
mylist = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
myset = set()
for element in mylist:
    myset.add(element)
print(myset)
"""


#字典的定义
#可以使用字典，实现用key取出Value的操作，不可以使用下标索引
"""
# 定义字典字面量(key不可以重复，新的key会覆盖之前的key)
{key:value,key:value,...,key:value}
# 定义字典变量
my_dict = {key:value,key:value,...,key:value}
# 定义空字典
my_dict = {}
my_dict = dict()

# 基于key获取value
语法：字典[key]
"""
"""
my_dict1 = {"王力宏":99,"周杰伦":88,"林俊杰":77}
my_dict2 = {}
my_dict3 = dict()
print(my_dict1)
print(my_dict2)
print(my_dict3)
print(my_dict1["王力宏"])
"""
#字典的嵌套
"""
stu_score_dict = {
    "王力宏":{
        "语文":77,
        "数学":66,
        "英语":33
    },
    "周杰伦": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    },
    "林俊杰": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    },
}
print(stu_score_dict)
print(stu_score_dict["周杰伦"]["语文"])
"""

#字典的常用操作
"""
1.新增元素
语法：字典[Key]=Value
结果：字典被修改，新增了元素

2.更新元素
语法：字典[Key]=Value
结果：字典被修改，新增了元素
注意：字典Key不可以重复，所以对已存在的Key执行上述操作，就是更新Value值

3.删除元素
语法：字典.pop(Key)
结果：获得指定Key的Value，同时字典被修改，指定Key的数据被修改

4.清空字典
语法：字典.clear()
结果：字典被修改，元素被清空

5.获取全部的Key
语法：字典.keys()
结果：得到字典中的全部Key

6.统计字典元素数量
语法：len(字典)
"""
"""
stu_score = {
    "王力宏": 77,
    "周杰伦": 88,
    "林俊杰": 99
}
#新增考试成绩
stu_score["张学友"] = 66
print(stu_score)

#更新王力宏的考试成绩
stu_score["王力宏"] = 100
print(stu_score)

#删除元素
score = stu_score.pop("周杰伦")
print(f"{score}\n{stu_score}")

#清空元素
stu_score.clear()
print(stu_score)

#获取全部Key
stu_score = {
    "王力宏": 77,
    "周杰伦": 88,
    "林俊杰": 99
}
print(stu_score.keys())

#遍历字典
#方式一：通过获取到全部的Key来完成遍历
for key in stu_score.keys():
    print(f"{key}:{stu_score[key]}")

#方式二：直接对字典进行for循环，每一次循环都是直接得到Key
for key in stu_score:
    print(f"{key}:{stu_score[key]}")

#统计字典元素数量
print(len(stu_score))
"""
#练习案例：升职加薪
"""
staff = {
    "王力宏":{
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰伦": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊杰": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学友": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(f"全体员工当前信息如下：\n{staff}")
for key in staff.keys():
    if staff[key]["级别"] == 1:
        staff[key]["级别"] = 2
        staff[key]["工资"] += 1000
print(f"全体员工级别为1的员工完成升职加薪操作，操作后：\n{staff}")
"""


"""
#5类数据容器的总结对比

1.是否支持下标索引
支持：列表、元组、字符串  --序列类型
不支持：集合、字典       --非序列类型

2.是否支持重复元素
支持：列表、元组、字符串  --序列类型
不支持：集合、字典       --非序列类型

3.是否可以修改
支持：列表、集合、字典
不支持：元组、字符串


基于各类容器的特点，他们的应用场景如下：
列表：一批数据，可修改、可重复的存储场景
元组：一批数据，可修改、不可重复的存储场景
字符串：一串字符的存储场景
集合：一批数据，去重存储场景
字典：一批数据，可用Key检索Value的存储场景
"""


#数据容器的通用操作
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = 'abcdefg'
my_set = {1,2,3,4,5}
my_dict={"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
# len元素个数
print(f"列表 元素个数有：{len(my_list)}")
print(f"元组 元素个数有：{len(my_tuple)}")
print(f"字符串 元素个数有：{len(my_str)}")
print(f"集合 元素个数有：{len(my_set)}")
print(f"字典 元素个数有：{len(my_dict)}")
print()

# max最大元素
print(f"列表 最大元素：{max(my_list)}")
print(f"元组 最大元素：{max(my_tuple)}")
print(f"字符串最大元素：{max(my_str)}")
print(f"集合 最大元素：{max(my_set)}")
print(f"字典 最大元素：{max(my_dict)}")
print()

# min最小元素
print(f"列表 最小元素：{min(my_list)}")
print(f"元组 最小元素：{min(my_tuple)}")
print(f"字符串最小元素：{min(my_str)}")
print(f"集合 最小元素：{min(my_set)}")
print(f"字典 最小元素：{min(my_dict)}")
print()

# 类型转换：容器转列表
"""
将给定容器转换为列表：list(容器)
将给定容器转换为元组：tuple(容器)
将给定容器转换为字符串：str(容器)
将给定容器转换为集合：set(容器)
"""

# 通用排序
"""
给指定容器进行排序：sorted(容器,[reverse=True])
注意：排序后结果变为列表对象，字典对象丢失Value
"""
"""
my_list = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = 'bdcefga'
my_set = {3,1,2,5,4}
my_dict={"key3":1,"key1":2,"key2":3,"key5":4,"key4":5}
print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")
print(f"列表对象的反向排序结果：{sorted(my_list,reverse=True)}")
print(f"元组对象的反向排序结果：{sorted(my_tuple,reverse=True)}")
print(f"字符串对象的反向排序结果：{sorted(my_str,reverse=True)}")
print(f"集合对象的反向排序结果：{sorted(my_set,reverse=True)}")
print(f"字典对象的反向排序结果：{sorted(my_dict,reverse=True)}")
"""

