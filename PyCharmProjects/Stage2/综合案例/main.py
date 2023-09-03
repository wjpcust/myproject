from pymysql import Connection
from data_define import Record
from file_define import FileReader,TextFileReader,JsonFileReader

text_file_read = TextFileReader("E:/PyCharmProjects/2011年1月销售数据.txt")
json_file_read = JsonFileReader("E:/PyCharmProjects/2011年2月销售数据JSON.txt")

jan_data = text_file_read.read_data()
feb_data = json_file_read.read_data()
all_data = jan_data + feb_data

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)
cursor = conn.cursor()
# cursor.execute("create database py_sql")
conn.select_db('py_sql')
# cursor.execute(
#     "create table orders("
#     "order_date date,"
#     "order_id varchar(255),"
#     "money int,"
#     "province varchar(10)"
#     ")"
# )
for data in all_data:
    cursor.execute(f"insert into orders values('{data.date}','{data.order_id}',{data.money},'{data.province}')")
conn.close()
