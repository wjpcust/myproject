# 异常的捕获
"""
1.捕获常规异常
基本语法：
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码

2.捕获指定异常
基本语法：
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')

注意：
如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
一般try下方只放一行尝试执行的代码

3.捕获多个异常
当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式进行书写
try:
    print(1/0)
except(NameError,ZeroDivisionError):
    print('ZeroDivision错误...')

4.捕获全部异常
try:
    print(1/0)
except Exception as e:
    print('出现异常了')

5.异常else
else表示的是如果没有异常要执行的代码
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')

6.异常的finally
finally表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    f = open('test.txt','r')
except Excption as e:
    f = open('test.txt','w')
else:
    print('没有异常')
finally:
    f.close()
"""
"""
# 基本捕获语法
try:
    f = open("E:/abc.txt","r",encoding='UTF-8')
except:
    print("出现异常了，因为文件不存在，我将open的模式改为w模式去打开")
    f = open("E:/abc.txt", "w", encoding='UTF-8')

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获多个异常
try:
    print(1/0)
except(NameError,ZeroDivisionError) as e:
    print('ZeroDivision错误...')

# 捕获全部异常
try:
    print(1/0)
except Exception as e:
    print('出现异常了')

# 异常else
try:
    print(1)
except Exception as e:
    print(e)
else:
    print('我是else，是没有异常的时候执行的代码')

# 异常的finally
try:
    f = open('123.txt','r',encoding='UTF-8')
except Exception as e:
    print('出现异常了')
    f = open('test.txt','w',encoding='UTF-8')
else:
    print('没有异常')
finally:
    f.close()
"""


# 异常的传递性
"""
def func01():
    print("这是func01开始")
    num = 1/0
    print("这是func01结束")

def func02():
    print("这是func02开始")
    func01()
    print("这是func02结束")

def main():
    try:
        func02()
    except Exception as e:
        print(e)

main()
"""


# 模块的概念和导入
"""
模块的作用：就是一个python文件，里面有类、函数、变量等，我们可以拿过来用（导入模块去使用）
模块的导入方式：
语法：
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
常用的组合形式如：
import 模块名
from 模块名 import 类、变量、方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名

1.import模块名
基本语法：
import 模块名
import 模块名1，模块名2
模块名.功能名()

2.from 模块名 import 功能名
基本语法：
from 模块名 import 功能名
功能名()

3.from 模块名 import * （*表示全部的意思）
基本语法：
from 模块名 import *
功能名()

4.as定义别名
基本语法：
# 模块定义别名
import 模块名 as 别名

# 功能定义别名
from 模块名 import 功能名 as 别名
"""
"""
import time
print('hello')
time.sleep(5)
print('hi')

from time import sleep
print('hello')
sleep(5)
print('hi')

from time import *
print('hello')
sleep(5)
print('hi')

import time as tt
print('hello')
tt.sleep(5)
print('hi')

from time import sleep as sl
print('hello')
sl(5)
print('hi')
"""


# 自定义模块并导入
# 制作自定义模块
"""
注意：每个python文件都可以作为一个模块，模块的名字就是文件的名字，也就是说自定义模块名必须要符合标识符命名规则
注意事项：当导入多个模块时，且模块内有同名功能，当调用这个同名功能的时候，调用的是后面导入的模块的功能

__main__：只有当前程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入
__all__：如果有一个文件中有'_all_'变量，当使用'from xxx import *'导入时，只能导入这个列表中的元素
"""
"""
import my_module1
my_module1.test(1,2)

from my_module2 import *
test_a(1,2)
"""


# 自定义python包
"""
import my_package.my_module1
# from my_package import my_module1
import my_package.my_module2
# from my_package import my_module2
my_package.my_module1.info_print1()
my_package.my_module2.info_print2()
# 通过__all__变量控制import*
"""


# 安装第三方包
"""
1.安装第三方包-pip
打开命令提示符，在里面输入：pip install 包名称，即可通过网络快速安装第三方包
可以通过如下命令，让其连接国内的网站进行包的安装：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

2.安装第三方包-pycharm
"""
# 练习案例：自定义工具包
import my_utils.str_util
import my_utils.file_util
print(my_utils.str_util.str_reverse('abcd'))
print(my_utils.str_util.substr('abcd', 1, 2))
my_utils.file_util.print_file_info('000.txt')
my_utils.file_util.append_to_file('E:/PyCharmProjects/word.txt', '哈哈哈哈哈')
my_utils.file_util.print_file_info('E:/PyCharmProjects/word.txt')