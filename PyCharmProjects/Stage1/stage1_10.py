# python基础综合案例


# json数据格式的转换
"""
json本质是一种特殊格式的字符串
json主要功能：就是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互。类似于：
    国际通用语言-英语
    中国56个名族不同地区的通用语言-普通话

1.json格式数据转化
# json数据的格式可以是：{"name":"admin","age":18}
# 也可以是：[{"name":"admin","age":18},{"name":"root","age":16},{"name":"张三","age":20}]

2.python数据和json数据的相互转化

# 导入json模块
import json

# 准备符合格式json格式要求的python数据
data = [{"name":"老王","age":16},{"name":"张三","age":20}]

# 通过json.dumps(data)方法把python数据转化为了json数据
data = json.dumps(data)

# 通过json.loads(data)方法把json数据转化为了python数据
data = json.loads(data)
"""
"""
import json
data = [{"name":"老王","age":16},{"name":"张三","age":20}]
data = json.dumps(data,ensure_ascii=False)
print(type(data))
print(data)
data = json.loads(data)
print(type(data))
print(data)
"""


# pyecharts的入门使用
"""
1.基础折线图
# 导包，导入Line功能构建折线图对象
from pyecharts.charts import Line
# 得到折线图对象
line = Line()
# 添加x轴数据
line.add_xaxis(["中国","美国","英国"])
# 添加y轴数据
line.add_yaxis("GDP",[30,20,10])
# 生成图表
line.render()

2.全局配置选项
set_global_opts方法，相应的选项和选项的功能如下：
TitleOpts：标题配置项
LegendOpts：图例配置项
ToolboxOpts：工具箱配置项
VisualMapOpts：视觉映射配置项
TooltipOpts：提示框配置项
DataZoomOpts：区域缩放配置项

3.系列配置项
"""
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
line = Line()
line.add_xaxis(["中国","美国","英国"])
line.add_yaxis("GDP",[30,20,10])
line.set_global_opts(
    title_opts=TitleOpts("GDP展示",pos_left="center",pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()
"""


# 数据准备
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts,LabelOpts
# 处理数据
f_us = open('E:/PyCharmProjects/美国.txt','r',encoding='UTF-8')
us_data = f_us.read()
f_jp = open('E:/PyCharmProjects/日本.txt','r',encoding='UTF-8')
jp_data = f_jp.read()
f_in = open('E:/PyCharmProjects/印度.txt','r',encoding='UTF-8')
in_data = f_in.read()
# 去掉不合json规范的开头
us_data = us_data.replace('jsonp_1629344292311_69436(','')
jp_data = jp_data.replace('jsonp_1629350871167_29498(','')
in_data = in_data.replace('jsonp_1629350745930_63180(','')
# 去掉不合json规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# json转python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']
# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]
# 获取确诊数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
# 生成图表
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data)   #x轴是公用的，所以使用一个国家的数据即可
# 添加y轴数据
line.add_yaxis('美国确诊人数',us_y_data,label_opts=LabelOpts(is_show=False))  #label_opts设置系列变量
line.add_yaxis('日本确诊人数',jp_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis('印度确诊人数',in_y_data,label_opts=LabelOpts(is_show=False))
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title='2020年美日印三国确诊人数对比折线图',pos_left='center',pos_bottom='1%'),
    toolbox_opts=ToolboxOpts(is_show=True)
)
line.render()
f_us.close()
f_jp.close()
f_in.close()