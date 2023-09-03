from matplotlib import pyplot as plt
from matplotlib import font_manager
import pandas as pd

file_path = "E:/Datasets/directory.csv"
plt.figure(figsize=(20,8),dpi=80)
pd.set_option("display.max_columns",None)
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/SIMHEI.TTF")

#中国每个城市店铺数量
df = pd.read_csv(file_path)

china = df[df['Country']=='CN']

province_data = china.groupby(by="City")['Brand'].count()[:25]

plt.bar(range(len(province_data.index)),province_data.values)

plt.xticks(range(len(province_data.index)),province_data.index,rotation=90,fontproperties=my_font)

plt.show()