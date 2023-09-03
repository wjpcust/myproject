from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

file_path = "E:/Datasets/directory.csv"
plt.figure(figsize=(20,8),dpi=80)
pd.set_option("display.max_columns",None)

#店铺前十国家
df = pd.read_csv(file_path)

country_data = df.groupby(by="Country")
country_data_count = country_data['Brand'].count()
count_sort = country_data_count.sort_values(ascending=False)

country = list(count_sort.index)[0:10]
num = list(count_sort)[0:10]

plt.bar(country,num)

plt.show()