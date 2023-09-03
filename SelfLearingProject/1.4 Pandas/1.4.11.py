from matplotlib import pyplot as plt
import pandas as pd

file_path = "E:/Datasets/books.csv"
pd.set_option("display.max_columns",None)
plt.figure(figsize=(20,8),dpi=80)

df = pd.read_csv(file_path)

print(df.info())

#去掉缺省数据
df = df[pd.notnull(df["original_publication_year"])]

year_data = df.groupby(by="original_publication_year")['books_count'].count()

print(year_data)

#不同年份书的平均评分
data = df["average_rating"].groupby(by=df["original_publication_year"]).mean()

x = data.index
y = data.values

plt.plot(range(len(x)),y)

plt.xticks(list(range(len(x)))[::10],x[::10].astype('int'),rotation=45)

plt.show()