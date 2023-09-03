#布尔类型和比较运算符
"""
bool_1 = True
bool_2 = False
print(f"bool_1变量的内容是：{bool_1}，类型是：{type(bool_1)}")
print(f"bool_2变量的内容是：{bool_2}，类型是：{type(bool_2)}")
"""


#if语句的基本格式
"""
age = 22
print(f"今年我已经{age}岁了")
if age >= 18:
    print("我已经成年了")
    print("即将步入大学生活")
print("时间过得真快")
"""
#练习案例：成年人判断
"""
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要补票10元。")
print("祝您游玩愉快。")
"""


#if else组合判断语句
"""
print("欢迎来到黑马儿童游乐场，儿童免费，成人收费。")
age = int(input("请输入你的年龄："))
if age>=18:
    print("您已成年，游玩需要补票10元。")
else:
    print("您未成年，可以免费游玩。")
print("祝您游玩愉快。")
"""
#练习案例：我要买票吗
"""
print("欢迎来到黑马动物园。")
height = int(input("请输入您的身高（cm）："))
if height > 120:
    print("您的身高超出120cm，游玩需要购票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快。")
"""


#if_elif_else组合使用的语法
"""
print("欢迎来到黑马动物园。")
if int(input("请输入您的身高（cm）：")) < 120:
    print("您的身高小于120cm，可以免费游玩。")
elif int(input("请输入您的vip级别（1~5）：")) > 3:
    print("您的vip等级大于3，可以免费游玩。")
elif int(input("请告所我今天几号：")) == 1:
    print("今天是1号，可以免费游玩。")
else:
    print("不好意思，所有条件都不满足，需要购票10元。")
print("祝您游玩愉快。")
"""
#练习案例：猜猜心里数字
"""
num = 10
if int(input("请输入第一次猜想的数字：")) == num:
    print("猜对了。")
elif int(input("不对，再猜一次：")) == num:
    print("猜对了。")
elif int(input("不对，再猜最后一次：")) == num:
    print("猜对了")
else:
    print(f"Sorry，全部猜错了，我想的是：{num}")
"""


#综合实战
import random
num = random.randint(1,10)
print("你有三次机会。")
num1 = int(input("请输入第一次猜想的数字："))
if num1 > num:
    print("大于目标数字，还剩两次机会。")
    num2=int(input("请输入第一次猜想的数字："))
    if num2 > num:
        print("大于目标数字，还剩一次机会。")
        if int(input("请输入第一次猜想的数字：")) != num:
            print("猜错了。")
        else:
            print("猜对了。")
    elif num2 < num:
        print("小于目标数字，还剩一次机会。")
        if int(input("请输入第一次猜想的数字：")) != num:
            print("猜错了。")
        else:
            print("猜对了。")
    else:
        print("猜对了。")
elif num1 < num:
    print("小于目标数字，还剩两次机会。")
    num2=int(input("请输入第一次猜想的数字："))
    if num2 > num:
        print("大于目标数字，还剩一次机会。")
        if int(input("请输入第一次猜想的数字：")) != num:
            print("猜错了。")
        else:
            print("猜对了。")
    elif num2 < num:
        print("小于目标数字，还剩一次机会。")
        if int(input("请输入第一次猜想的数字：")) != num:
            print("猜错了。")
        else:
            print("猜对了。")
    else:
        print("猜对了。")
else:
    print("猜对了。")