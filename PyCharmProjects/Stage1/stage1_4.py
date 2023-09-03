#while循环的基础运用
"""
i = 1
while i <= 100:
    print(f"第{i}次")
    i += 1
"""
#练习案例：求1-100的和
"""
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)
"""
#练习案例：猜数字
"""
import random
num = random.randint(1,100)
num_1 = int(input("输入猜测数字："))
sum = 1
while num_1 != num:
    if num_1 < num:
        print("小于目标数字。")
    else:
        print("大于目标数字。")
    num_1 = int(input("输入猜测数字："))
    sum += 1
print(f"猜对了，共猜了{sum}次。")
"""


#while循环的嵌套案例：九九乘法表
"""
i = 1
while i < 10:
    j = 1
    while j <= i:
        #end=''  不换行
        print(f"{j}*{i}={i*j}\t",end='')
        j += 1
    print()
    i += 1
"""


#for循环的基础语法
"""
name = "itheima"
for x in name:
    print(x)
"""
#练习案例：数一数有几个a
"""
name = "itheima is a brand of itcast"
sum = 0
for x in name:
    if x == "a":
        sum += 1
print(f"共有{sum}个a")
"""

#range语句
"""
语法1：
range(num)
获取一个从0开始，到num结束的数字序列（不包含num本身）
如，range(5)取得的数据是：[0,1,2,3,4]

语法2：
range(num1,num2)
获得一个从num1开始，到num2结束的数字序列（不包含num2本身）
如，range(5,10)取得的数据是：[5,6,7,8,9]

语法3：
range(num1,num2,step)
获得一个从num1开始，到num2结束的数字序列（不包含num2本身）
数字之间的步长，以step为准（step默认为1）
如，range(5,10,2)取得的数据是：[5,7,9]
"""
#练习案例：有几个偶数
"""
num = 100
sum = 0
for x in range(1,num):
    if x % 2 == 0:
        sum += 1
print(f"1到{num}（不含{num}本身）范围内，有{sum}个偶数。")
"""

#for循环的嵌套应用：九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end='')
    print()
"""


#循环中断：break和continue
#循环综合案例：发工资
import random
sum = 10000
num = random.randint(1,10)
for i in range(1,21):
    if sum == 0:
        print("工资发完了，下个月领取吧。")
        break
    elif num >= 5:
        sum -= 1000
        num = random.randint(1, 10)
        print(f"向员工{i}发放工资1000元，账户余额还剩余{sum}元")
    elif num < 5:
        print(f"员工{i}，绩效分{num}，不发工资，下一位。")
        num = random.randint(1, 10)