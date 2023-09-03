# 初识对象
"""
# 使用对象组织数据
1.设计类（class）
class Student:
    name = None         # 记录学生姓名
2.创建对象
# 基于类创建对象
stu_1 = Student()
stu_2 = Student()
3.对象属性赋值
stu_1.name = "周杰伦"      # 为学生1对象赋予名称属性值
stu_2.name = "林俊杰"      # 为学生2对象赋予名称属性值
"""
"""
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None
stu_1 = Student()
stu_1.name = "林俊杰"
stu_1.gender = "男"
stu_1.nationality = "中国"
stu_1.native_place = "山东省"
stu_1.age = 31
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
"""


# 类的成员方法
"""
# 类的定义和使用
1.语法：
class 类名称:      #class是关键字，表示要定义类了
    类的属性        #即定义在类中的变量（成员变量）
    类的行为        #即定义在类中的函数（成员方法）

2.创建类对象的语法：
对象 = 类名称()

3.成员方法的定义语法
def 方法名(self,形参1,......,形参N):
    方法体
self关键字是成员方法定义的时候，必须填写的
它用来表示类对象自身的意思
当我们使用类对象调用方法时，self会自动被python传入
在方法内部，想要访问类的成员变量，必须使用self
传参时可忽略self
"""
"""
class Student:
    name = None
    def say_hi(self):
        print(f"大家好，我是{self.name}")
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name}，{msg}")
stu = Student()
stu.name = "毛不易"
stu.say_hi()
stu.say_hi2("一杯敬自由")
stu2 = Student()
stu2.name = "王维家"
stu2.say_hi()
stu2.say_hi2("一杯敬死亡")
"""


# 类和对象
"""
class clock:
    id = None
    price = None
    def ring(self):
        import winsound
        winsound.Beep(2000,3000)
clock1 = clock()
clock1.id = '003020'
clock1.price = 19.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()
"""


# 构造方法
"""
python类可以使用：__init__()方法，称之为构造方法
可以实现：
    在创建类对象（构造类）的时候，会自动执行。
    在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
"""
"""
class Student:
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")
stu = Student('毛不易','28','18500006666')
print(stu.name)
print(stu.age)
print(stu.tel)
"""
# 练习案例：学生信息录入
"""
class Student:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
for i in range(10):
    print(f"当前录入第{i+1}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名：")
    age = int(input("请输入学生姓名："))
    address = input("请输入学生地址：")
    stu = Student(name,age,address)
    print(f"学生{i+1}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}】")
"""


# 魔术方法
"""
1.__str__字符串方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student = Student("周杰伦",11)
print(student)      #结果：<__main__.Student object at 0x000002200CFD7040>
print(str(student)) #结果：<__main__.Student object at 0x000002200CFD7040>
当类对象需要转换为字符串之时，会输出如上结果（内存地址）
内存地址没多大用，我们可以通过__str__方法，控制类转换为字符串的行为。
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student类对象，name={self.name}，age={self.age}"
student = Student("周杰伦",11)
print(student)      #结果：Student类对象，name=周杰伦，age=11
print(str(student)) #结果：Student类对象，name=周杰伦，age=11

2.__lt__小于符号比较方法
直接对2个对象进行比较是不可以的，但在类中实现__lt__方法，既可同时完成：小于符号和大于符号2种比较
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __lt__(self,other):
        return self.age < other.age
stu1=Student("周杰伦",11)
stu2=Student("林俊杰",13)
print(stu1 < stu2)  # 结果：True
print(stu1 > stu2)  # 结果：False

3.__le__小于等于比较符号方法
魔术方法：__le__可用于：<=、>=两种比较运算符上
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __le__(self,other):
        return self.age <= other.age
stu1=Student("周杰伦",11)
stu2=Student("林俊杰",13)
print(stu1 <= stu2)  # 结果：True
print(stu1 >= stu2)  # 结果：False

4.__eq__比较运算符实现方法
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __eq__(self,other):
        return self.age == other.age
stu1=Student("周杰伦",11)
stu2=Student("林俊杰",11)
print(stu1 == stu2)  # 结果：True
不实现__eq__方法，对象之间可以比较，但是是比较内存地址，也即是：不同对象==比较一定是False结果
实现了__eq__方法，就可以按照自己的想法来决定2个对象是否相等了
"""
"""
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __str__(self):
        return f"Student类对象，name={self.name}，age={self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other):
        return self.age <= other.age

    # __eq__魔术方法
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("周杰伦",31)
stu2 = Student("林俊杰",36)
stu3 = Student("毛不易",31)
print(stu1)
print(str(stu1))
print(stu1 < stu2)
print(stu1 >= stu2)
print(stu1 == stu3)
"""

# 面向对象包含3大主要特性：
# 封装
# 继承
# 多态

# 封装
"""
1.封装：表示的是，将现实世界事物的属性、行为，封装到类中，描述为成员变量、成员方法，从而完成程序对现实世界事物的描述

2.私有成员：不公开的属性和行为
私有成员变量
私有成员方法
定义私有成员的方式：
    私有成员变量：变量名以__开头
    私有成员方法：方法名以__开头
私有成员无法被类对象使用，但是可以被其他的成员使用
在类中提供仅供内部使用的属性和方法，而不对外开放（类对象无法使用）
"""
"""
class Phone:
    __current_voltage = 0.5
    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已设置为单核运行进行省电")

phone = Phone()
phone.call_by_5g()
"""
# 练习案例：设计带有私有成员的手机
"""
class Phone:
    __is_5g_enable = False
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()
"""


# 继承的基础语法
"""
1.单继承
class Phone:
    IMEI = None
    producer = None
    
    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = True
    
    def call_by_5g(self):
        print("2022最新5g通话")
        
语法：
class 类名(父类名):
    类内容体
继承分为：单继承和多继承
继承表示：将从父类那里继承（复制）来成员变量和成员方法（不含私有）

2.多继承
一个类继承多个父类
语法：
class 类名(父类1,父类2,......,父类N):
    类内容体
注意：多个父类中，如果有同名的成员，那么默认以继承顺序（从左到右）为优先级。
即：先继承的保留，后继承的被覆盖
pass：占位语句，用来保证函数（方法）或类定义的完整性，表示无内容，空的意思
"""
# 单继承
"""
class Phone:
    IMEI = None
    producer = "Ittest"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10001"

    def call_by_5g(self):
        print("2022最新5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 多继承
class NFCreader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")

class MyPhone(Phone,NFCreader,RemoteControl):
    pass        #用来补充语法

phone = MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
print(phone.producer)
"""


# 复写父类成员和调用父类成员
"""
1.复写：子类继承父类的成员属性和成员方法后，如果对其“不满意”，那么可以进行复写
即：在子类中重新定义同名的属性或方法即可

2.调用父类同名成员
一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
如果需要使用被复写的父类的成员，需要特殊的调用方式：
方式1：调用父类成员
    使用成员变量：父类名.成员变量
    使用成员方法：父类名.成员方法(self)
方式2：使用super()调用父类成员
    使用成员变量：super().成员变量
    使用成员方法：super().成员方法()
"""
"""
class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        # 方式1
        print(f"父类的厂商是{Phone.producer}")
        Phone.call_by_5g(self)
        # 方式2
        print(f"父类的厂商是：{super().producer}")
        super().call_by_5g()
        print("关闭CPU单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)
"""


#　变量的类型注解
"""
1.类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）
主要功能：
    帮助第三方IDE工具（如PyCharm）对代码进行类型推断，协助做代码提示
    帮助开发者自身对变量进行类型注释
支持：
    变量的类型注解
    函数（方法）形参列表和返回值的类型注解

2.为变量设置类型注解
基础语法：变量:类型
# 基础数据类型注解：
var_1:int = 10
var_2:float = 3.1415926
var_3:bool = True
var_4:str = "itheima"
# 类对象类型注解：
class Student:
    pass
stu:Student = Student()
# 基础容器类型注解：
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_set:set = {1,2,3}
my_dict:dict = {"itheima":666}
my_str:str = "itheima"
# 容器类型详细注解：
my_list:list[int]= [1,2,3]
my_tuple:tuple[str,int,bool] = ("itheima",666,True)
my_set:set[int] = {1,2,3}
my_dict:dict[str,int] = {"itheima":666}
注意：
    元组类型设置类型详细注解，需要将每一个元素都标记出来
    字典类型设置类型详细注解，需要2个类型，第一个是key，第二个是value

除了使用 变量:类型，这种语法作注解外，也可以在注释中进行类型注解
语法：#type:类型
# 在注释中进行类型注解
class Student:
    pass
    
var_1 = random.randint(1,10)    # type:int
var_2 = json.loads(data)        # type:dict[str,int]
var_3 = func()                  # type:Student

3.类型注解的限制
并不会真正的对类型做验证和判断，类型注解仅仅是提示性的，不是决定性的
var_1:int = "itheima"
是不会报错的
"""
"""
import random
import json
# 基础数据类型注解：
var_1:int = 10
var_2:float = 3.1415926
var_3:bool = True
var_4:str = "itheima"
# 类对象类型注解：
class Student:
    pass
stu:Student = Student()
# 基础容器类型注解：
my_list:list = [1,2,3]
my_tuple:tuple = (1,2,3)
my_set:set = {1,2,3}
my_dict:dict = {"itheima":666}
my_str:str = "itheima"
# 容器类型详细注解：
my_list:list[int]= [1,2,3]
my_tuple:tuple[str,int,bool] = ("itheima",666,True)
my_set:set[int] = {1,2,3}
my_dict:dict[str,int] = {"itheima":666}
# 在注释中进行类型注解
var_1 = random.randint(1,10)    # type:int
var_2 = json.loads('{"name":"zhangsan"}')        # type:dict[str,int]
def func():
    return 10
var_3 = func()      # type:int
"""


# 函数和方法类型注解
"""
函数和方法的形参类型注解语法：
def 函数方法名(形参名:类型,形参名:类型,......):
    pass
    
同时，函数（方法）的返回值也是可以添加类型注解的。语法如下：
def 函数方法名(形参:类型,......,形参:类型) -> 返回值类型:
    pass
"""
"""
def add(x:int,y:int):
    return x + y
add(5,6)

def func(data:list) -> list:
    return data
"""


# Union联合类型注解
"""
使用Union[类型,......,类型]，可以定义联合类型注解
from typing import Union
my_list:list[Union[str,int]] = [1,2,"itheima","itcast"]
my_dict:dict[str,Union[str,int]] = {"name":"周杰伦","age":31}

Union联合类型注解，在变量注解、函数（方法）形参和返回值注解中，均可使用。
def func(data:Union[int,str]) -> Union[int,str]:
    pass
"""
"""
from typing import Union
my_list:list[Union[int,str]] = [1,2,"itheima","itcast"]
def func(data:Union[int,str]) -> Union[int,str]:
    pass
"""


# 多态
"""
1.同样的行为（函数），传入不同的对象，得到不同的状态，常用在继承关系上，如：
    函数（方法）形参声明接收父亲对象
    实际传入父类的子类对象进行工作
即：
    以父类做定义声明
    以子类做实际工作
    用以获得同一行为，不同状态
    
2.抽象类（也可以称之为接口）
父类用来确定有哪些方法
具体的方法，由子类自行决定

抽象类：含有抽象方法的类称之为抽象类，好比定义一个标准，包含了一些抽象的方法，要求子类必须实现
抽象方法：方法是空实现的（pass）称之为抽象方法
配合多态，完成：
    抽象的父类设计（设计标准）
    具体的子类实现（实现标准）
"""
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swing_l_r(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)
"""


# 数据分析案例步骤1-文件读取
"""
面向对象，数据分析案例，主业务逻辑代码
实现步骤：
1.设计一个类，可以完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件，产生数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过PyEcharts进行图形绘制
"""