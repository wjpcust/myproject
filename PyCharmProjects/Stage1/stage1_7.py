# 函数的多返回值
"""
def test_return():
    return 1,"hello"
x,y = test_return()
print(x)
print(y)
"""
"""
按照返回值的顺序，写对应顺序的多个变量接收即可
变量之间用逗号隔开
支持不同类型的数据return
"""


# 函数的多种参数的使用方式
"""
1.位置参数：调用函数时根据函数定义的参数位置来传递参数
def user_info(name,age,gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
user_info('TOM',20,'男')

2.关键字参数：函数调用时通过“键=值”形式传递参数
作用：可以让函数更加清晰、容易使用，同时也清楚了函数的顺序需求
def user_info(name,age,gender):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')

# 关键字传参
user_info(name="小明",age=20,gender="男")
# 可以不按固定顺序
user_info(age=20,gender="男",name="小明")
# 可以和位置参数混用，位置参数必须在前，且匹配参数顺序
user_info("小明",age=20,gender="男")

3.缺省参数：也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）
作用：当调用函数时没有传递参数，就会使用默认是用缺省参数对应的值
def user_info(name,age,gender='男'):
    print(f'您的名字是{name}，年龄是{age}，性别是{gender}')
user_info('TOM',20)
user_info('ROSE',18,'女')

4.不定长参数：不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数（不传参也可以）的场景
作用：当调用函数时不确定参数个数时，可以使用不定长参数
不定长参数的类型：位置传递、关键字传递
# 位置传递
def user_info(*args):
    print(args)
user_info('TOM')
user_info('TOM',18)
注意：传进的所有参数都会被args变量收集，他会根据传进参数的位置合并为一个元组（tuple），args是元组类型，这就是位置传递

# 关键字传递
def user_info(**kwargs):
    print(kwargs)
user_info(name='TOM',age=18,id=110)
注意：参数是“键=值”形式的情况下，所有的“键=值”都会被kwargs接收，同时会根据“键=值”组成字典
"""


# 函数作为参数传递
"""
def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return x + y
test_func(compute)
"""


# lambda匿名函数
"""
函数的定义中：
def关键字，可以定义带有名称的函数
lambda关键字，可以定义匿名函数（无名称）
有名称的函数，可以基于名称重复使用
无名称的匿名函数，只可临时使用一次

匿名函数定义语法：
lambda 传入参数:函数体(一行代码)
lambda是关键字，表示定义匿名函数
传入参数表示匿名函数的形式参数，如：x,y表示接收2个形式参数
函数体，就是函数的执行逻辑，要注意：只能写一行，无法写多行代码
"""
def test_func(compute):
    result = compute(1,2)
    print(result)
test_func(lambda x,y: x + y) #无法二次使用