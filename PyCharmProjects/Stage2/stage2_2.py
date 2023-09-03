# SQL基础和DDL
"""
SQL语法特征
1.大小写不敏感
2.可以单行或多行书写，最后以;结束
3.支持注释：
    单行注释：-- 注释内容（--后面一定要有一个空格）
    单行注释：#注释内容（#后面可以不加空格，推荐加上）
    多行注释：/* 注释内容 */

DDL - 库管理
1.查看数据库：show databases;
2.使用数据库：use 数据库名称;
3.创建数据库：create database 数据库名称 [charset UTF-8];
4.删除数据库：drop database 数据库名称;
5.查看当前使用的数据库：select database();

DDL - 表管理
1.查看有哪些表：show tables;  注意：需要先选择数据库
2.删除表：drop table 表名称;
        drop table if exists 表名称;
3.创建表：
create table 表名称(
    列名称 列类型,
    列名称 列类型,
    ......
);
类型有：
        int                 -- 整数
        float               -- 浮点数
        varchar(长度)        -- 文本，长度为数字，做最大长度限制
        date                -- 日期类型
        timestamp           -- 时间戳类型


DML
1.数据插入INSERT
基础语法：
insert into 表[(列1,列2,......,列n)] values(值1,值2,......,值n)[,(值1,值2,......,值n),......,(值1,值2,......,值n)]

2.数据删除DELETE
基础语法：
delete from 表名称 [where 条件判断]
条件判断：列 操作符 值
操作符：= < > <= >= !=等等

3.数据更新UPDATE
基础语法：
uodate 表名 set 列=值 [where 条件判断];


DQL - 基础查询
1.基础数据查询
基础语法：
select 字段列表|* from 表

2.基础查询 - 过滤
语法：
select 字段列表|* from 表 where 条件判断


DQL - 分组聚会
1.分组聚合
基础语法：
select 字段|聚合函数 from 表 [where 条件] group by 列
注意：group by中出现了哪个列，哪个列才能出现在select中的非聚合中
聚合函数：
- SUM(列) 求和
- AVG(列) 求平均值
- MIN(列) 求最小值
- MAX(列) 求最大值
- COUNT(列|*) 求数量


DQL - 排序分页
1.结果排序
基础语法：
select 列|聚合函数|* from 表
where ...
group by ...
order by ... [asc|desc]

2.结果分页限制
可以使用limit关键字，对查询结果进行数量限制或分页显示
基础语法：
select 列|聚合函数|* from 表
where ...
group by ...
order by ... [asc|desc]
limit n[,m]


截至到目前学习到的关键字，需注意：
    where、group by、order by、limit均可按需求省略
    select和from是必写的
    执行顺序：from > where > group by和聚合函数 > select > order by > limit
"""


# python操作MySQL基础使用
"""
1.创建到MySQL的数据库连接
代码如下：
from pymysql import Connection
# 获取到MySQL数据库的链接对象
conn = Connection(
    host = 'localhost',     # 主机名（或IP地址）
    port = 3306,            # 端口，默认3306
    user = 'root',          # 账户名
    password = '123456'     # 密码
)
# 打印MySQL数据库软件信息
print(conn.get_server_info())
# 关闭到数据库的链接
conn.close()

2.执行SQL语句
执行非查询性质的SQL语句：
# 获取游标对象
cursor = conn.cursor()
conn.select_db("test")      # 先选择数据库
# 使用游标对象，执行SQL语句
cursor.execute("create table test_pymysql(id int,info varchar(255))")

执行查询性质的SQL语句：
# 使用游标对象，执行SQL语句
cursor.execute("select * from star")
# 获取查询结果
result: tuple = cursor.fetchall()
for r in result:
    print(r)
"""
"""
from pymysql import Connection
# 获取到MySQL数据库的链接对象
conn = Connection(
    host = 'localhost',     # 主机名（或IP地址）
    port = 3306,            # 端口，默认3306
    user = 'root',          # 账户名
    password = '123456'     # 密码
)
# 打印MySQL数据库软件信息
# print(conn.get_server_info())
# 获取游标对象
cursor = conn.cursor()
conn.select_db("world")      # 先选择数据库
# # 使用游标对象，执行SQL语句
# cursor.execute("create table test_pymysql(id int,info varchar(255))")
# 使用游标对象，执行SQL语句
cursor.execute("select * from star")
# 获取查询结果
result: tuple = cursor.fetchall()
for r in result:
    print(r)
# 关闭到数据库的链接
conn.close()
"""


# python操作MySQL数据插入
"""
1.commit提交
pymysql在执行数据插入或其他产生数据更改的SQL语句时，默认是需要提交更改的，即需要通过代码”确认“这种更改行为
通过链接对象.commit()即可确认此行为

2.自动commit
可以在构建链接对象的时候，设置自动commit的属性
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True         # 设置自动提交
)
"""
"""
from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True
)
cursor = conn.cursor()
conn.select_db('world')
cursor.execute('insert into star values(10022,"王维家",28,"男")')
# conn.commit()
cursor.close()
"""


# 反向输出
from pymysql import Connection
import json
f = open('E:/PyCharmProjects/py_sqlJSON.txt','w',encoding='UTF-8')
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)
conn.select_db('py_sql')
cursor = conn.cursor()
cursor.execute('select * from orders')
result = cursor.fetchall()
for r in result:
    dict = {"date":str(r[0]),"order_id":r[1],"money":r[2],"province":r[3]}
    f.write(json.dumps(dict,ensure_ascii=False))
    f.write('\n')
f.close()
conn.close()