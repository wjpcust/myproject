#python中__call__的用法

class Person:
    def __call__(self, name):
        print("__call__"+"Hello"+name)

    def hello(self,name):
        print("hello"+name)

person = Person()
person("zhnagsan")
person.hello("lisi")