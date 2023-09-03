# 基础柱状图构建
# 通过Bar构建基础柱状图
"""
from pyecharts.charts import Bar
from pyecharts.options import *
bar = Bar()
bar.add_xaxis(['中国','美国','英国'])
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position='right'))
# 反转x轴和y轴
bar.reversal_axis()
bar.render("基础柱状图.html")
"""


# 基础时间线柱状图绘制
"""
from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
bar1 = Bar()
bar1.add_xaxis(['中国','美国','英国'])
bar1.add_yaxis('GDP',[30,20,10],label_opts=LabelOpts(position='right'))
bar1.reversal_axis()
bar2 = Bar()
bar2.add_xaxis(['中国','美国','英国'])
bar2.add_yaxis('GDP',[50,30,20],label_opts=LabelOpts(position='right'))
bar2.reversal_axis()
bar3 = Bar()
bar3.add_xaxis(['中国','美国','英国'])
bar3.add_yaxis('GDP',[70,60,60],label_opts=LabelOpts(position='right'))
bar3.reversal_axis()
# 创建时间线对象，设置主题
timeline = Timeline(
    {'theme':ThemeType.LIGHT}
)
# timeline对象添加bar柱状图
timeline.add(bar1,'2021年GDP')
timeline.add(bar2,'2022年GDP')
timeline.add(bar3,'2023年GDP')
# 设置自动播放
timeline.add_schema(
    play_interval=1000,     #自动播放时间间隔
    is_timeline_show=True,  #是否在自动播放的时候，显示时间线
    is_auto_play=True,      #是否自动播放
    is_loop_play=True       #是否循环自动播放
)
# 通过时间线绘图
timeline.render("基础柱状图-时间线.html")
"""


# 动态GDP柱状图绘制
# 列表的sort方法
"""
使用方式：
列表.sort(key=选择排序依据的函数,reverse=True|False)
参数key，是要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据
参数reverse，是否要反转排序结果，True表示降序，False表示升序
"""
"""
my_list = [['a',33],['b',55],['c',11]]
# def choose_sort_key(element):
#     return element[1]
# my_list.sort(key=choose_sort_key,reverse=True)
my_list.sort(key=lambda element:element[1],reverse=True)
print(my_list)
"""

from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
f = open('E:/PyCharmProjects/1960-2019全球GDP数据.csv','r',encoding='GB2312')
data_lines = f.readlines()
f.close()
# 删除第一行
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 年份: [ [国家,gdp],[国家,gdp], .....], 年份: [ [国家,gdp],[国家,gdp], .....], ......}
data_dict={}
for line in data_lines:
    year = int(line.split(",")[0])      #年份
    country = line.split(",")[1]        #国家
    gdp = float(line.split(",")[2])            #gdp
    #如何判断字典里有没有指定的key
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])
# 排序年份
timeline = Timeline({"theme":ThemeType.LIGHT})
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key = lambda element:element[1],reverse=True)
    # 去除本年份前八名的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1] / 100000000)
    # 构建柱状图对象
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis('GDP(亿）',y_data,label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    # 设置每一年的图标标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP前8数据")
    )
    timeline.add(bar,str(year))
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("1960-2019全球GDP前8国家.html")