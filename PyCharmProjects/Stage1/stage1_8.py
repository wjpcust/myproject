# 文件编码概念
# 文件的读取操作
"""
1.open()打开函数
可以打开一个已经存在的文件，或者创建一个新文件
语法：open(name,mode,encoding)
name：是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
mode：设置打开文件的模式（访问模式）：只读、写入、追加等
encoding：编码格式（推荐使用UTF-8）

# mode常用的三种基础访问模式：
r   ：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w   ：打开一个文件只用于写入。如果该文件已存在则打开文件，并从头开始编辑，原有内容会被删除。如果该文件不存在，创建新文件。
a   ：打开一个文件用于追加。如果该文件已存在，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。

# 读取操作相关方法
1.read()方法
语法：文件对象.read(num)
num表示要从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据

2.readlines()方法
readlines可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素

3.readline()方法
一次读取一行内容

4.for循环读取文件行
for line in open("python.txt","r"):
    print(line)

5.close()关闭文件对象，停止文件占用
语法：文件对象.close()

6.withopen()
语法：with open("python.txt","r") as f:
        f.readlines()
通过在with open的语句块中对文件进行操作
可以在操作完成后自动关闭close文件，避免忘掉close方法
"""
"""
# encoding的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
f = open('E:/PyCharmProjects/python.txt','r',encoding="UTF-8")
print(type(f))
print(f"读取10个字节的结果：{f.read(10)}")
print(f"读取全部内容的结果：{f.read()}")
f.close()

f = open('python.txt','r',encoding='UTF-8')
lines = f.readlines()
print(f"lines对象的内容是：{lines}")
f.close()

f = open('python.txt','r',encoding='UTF-8')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}")
print(f"第三行的数据是：{line3}")
f.close()

f = open('python.txt','r',encoding='UTF-8')
for line in f:
    print(line)
f.close()

with open('python.txt','r',encoding='UTF-8') as f:
    for line in f:
        print(line)
"""
# 课后练习：单词计数
"""
sum = 0
with open('word.txt','r',encoding='UTF-8') as f:
    for line in f:
        sum += line.strip().split(" ").count("itheima")
print(sum)
"""
"""
sum = 0
with open('word.txt','r',encoding='UTF-8') as f:
    sum = f.read().count("itheima")
print(sum)
"""


# 文件的写入操作
"""
案例演示：
# 1.打开文件
f=open("python.txt","w")

# 2.文件写入
f.write('hello world')

# 3.内容刷新
f.flush()  #close内置了flush功能

注意：
直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
当调用flush时，内容会真正写入文件
这样做避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写磁盘）
"""
"""
f = open('test.txt','w',encoding='UTF-8')
f.write("Hello World!!!")
f.flush()
f.close()  #close内置了flush功能
"""


# 文件的追加操作
"""
案例演示：
# 1.打开文件
f=open("python.txt","a")

# 2.文件写入
f.write('hello world')

# 3.内容刷新
f.flush()  #close内置了flush功能

注意：
a模式，文件不存在会创建文件
a模式，文件存在会在最后，追加写入文件
"""
"""
f = open('test.txt','a',encoding='UTF-8')
f.write("\nfighting!!!")
f.close()  #close内置了flush功能
"""

f1 = open('bill.txt','r',encoding='UTF-8')
f2 = open('bill.txt.bak','w',encoding='UTF-8')
for line in f1:
    if line.strip().split(',')[4] == "测试":
        continue
    f2.write(line)
f1.close()
f2.close()