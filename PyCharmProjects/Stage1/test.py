"""
num_str = str(11)
print(type(num_str),num_str)
str_num = int("11")
print(type(str_num),str_num)
str_float = float("11.345")
print(type(str_float),str_float)
#指数
print("10的二次幂：",10**2)
#整除
print("11 // 2 = ",11//2)
print("8 / 4 =",8/4)
"""

#字符串扩展
"""
name = "黑马程序员"
address = "长春"
tel = 123456789
num = 57
print("我是"+ name + ",来自：" + address + ",电话：%s,%s" %(tel,num))

name_1 = "传智播客"
setup_year = 2006
stock_price = 19.99
print("%s，成立于%d年，股价为%.2f" % (name_1,setup_year,stock_price))
#字符串格式化方式：f"{占位}"（不做精度控制）
print(f"{name_1}，成立于{setup_year}年，股价为{stock_price}")
print("1 * 1 的结果是：%d" % (1*1))
print(f"1 * 2的结果是：{1 * 2}")
print("字符串在python中的类型名是：%s" % (type("字符串")))
"""
#练习：股价计算小程序
"""
name = "传智播客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (stock_price_daily_growth_factor,growth_days,stock_price*stock_price_daily_growth_factor**growth_days))
"""
name = input("请输入姓名：")
print("姓名：%s" % name)
#输入默认为字符串类型
num = input("请输入密码：")
print(f"密码：{num}，类型为：{type(num)}")
num = int ( num )
print(f"密码：{num}，类型为：{type(num)}")

