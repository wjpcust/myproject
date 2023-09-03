# item_one = 1
# item_two = 2
# item_three = 3
# total = item_one + \
#         item_two + \
#         item_three
# str1 = 'hello'
# print(str1*2)
# list = ['runoob',1,2,'john']
# list[2] = 6
# tuple1 = ('runoob',1,2,'john')
# # tuple1[2] = 6
# print(list[::-1])
# print(tuple1)
# dict1 = {'name':'runoob','code':6734,'dept':'sales'}
# print(dict1.keys())
# print(dict1.values())
# a = 21
# b = 10
# print(a/b)
# print(a//b)
# print(a and b)
# print(a or b)
# print(not(a and b))

import time
import calendar
print(time.asctime(time.localtime(time.time())))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
print(calendar.month(2023,7))