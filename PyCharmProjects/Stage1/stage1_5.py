#函数初体验
"""
str1 = "itheima"
str2 = "cust"
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串长度为{count}。")
my_len(str1)
my_len(str2)
"""

#函数的基础定义语法
"""
def 函数名(传入参数):
    函数体
    return 返回值
"""
#练习案例：自动查核酸
"""
def check():
    print("欢迎来到黑马程序员！\n请出示您的健康码以及72小时核算证明！")
check()
"""


#函数的传入参数
"""
def add(x,y):
    result = x + y
    print(f"{x}+{y}={result}")
add(5,9)
add(1,2)
"""
#练习案例：升级版自动查核酸
"""
def check(x):
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核算证明，并配合测量体温！")
    if x <= 37.5:
        print(f"体温测量中，您的体温是：{x}度，体温正常请进！")
    else:
        print(f"体温测量中，您的体温是：{x}度，需要隔离！")
check(37.3)
check(39.3)
"""


#函数的返回值定义语法
"""
def 函数(参数...)
    函数体
    return 返回值
    
变量 = 函数(参数)
"""
"""
def add(x,y):
    result = x + y
    return result
r = add(5,7)
print(r)
"""


#函数的嵌套调用
"""
def func_b():
    print("---2---")
def func_a():
    print("---1---")
    func_b()
    print("---3---")
func_a()
"""


#综合案例：黑马ATM
sum = 5000000
name = input("请输入您的姓名：")
def ye(x):
    print("---------------查询余额------------------")
    print(f"{name}，您好，您的余额剩余：{x}元")

def cun(x):
    global sum
    sum += x
    print("-----------------存款------------------")
    print(f"{name}，您好，您存款{x}元成功")
    print(f"{name}，您好，您的余额剩余：{sum}元")

def qu(x):
    global sum
    sum -= x
    print("-----------------取款------------------")
    print(f"{name}，您好，您取款{x}元成功")
    print(f"{name}，您好，您的余额剩余：{sum}元")

def menu():
    print("----------------主菜单-----------------")
    print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    choose = int(input("请输入您的选择："))
    if choose == 1:
        ye(sum)
    elif choose == 2:
        num_1 = int(input("输入存款金额："))
        cun(num_1)
    elif choose == 3:
        num_2 = int(input("输入取款金额："))
        qu(num_2)
    else:
        return True

flag = False
while not flag:
    flag = menu()
print("程序退出")