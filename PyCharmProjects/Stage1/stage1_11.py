# 数据可视化案例-地图-基础地图使用
# 基础地图演示
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("台湾省",199),
    ("安徽省",299),
    ("广州省",399),
    ("湖北省",599)
]
map.add("地图",data,"china")
# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":9,"label":"1-9","color":"#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FF6666"},
            {"min":100,"max":500,"label":"100-500","color":"#990033"}
        ]
    )
)
map.render()
"""


# 国内疫情地图
from pyecharts.charts import Map
from pyecharts.options import *
import json
f = open("E:/PyCharmProjects/疫情.txt","r",encoding="UTF-8")
f_data = f.read()
f.close()
f_dict = json.loads(f_data)["areaTree"][0]["children"]
data_list = []
for province in f_dict:
    province_name = province["name"] + "省"
    province_confirm = province["total"]["confirm"]
    data_list.append((province_name,province_confirm))
map = Map()
map.add("各省份确诊人数",data_list,"china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"}
        ]
    )
)
map.render("全国疫情地图.html")



# 省级地图绘制
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *
f = open('E:/PyCharmProjects/疫情.txt','r',encoding='UTF-8')
f_data = f.read()
f.close()
f_dict = json.loads(f_data)['areaTree'][0]['children'][24]['children']
jl_list = []
for jl_data in f_dict:
    jl_name = jl_data["name"] + "市"
    jl_confirm = jl_data["total"]["confirm"]
    jl_list.append((jl_name,jl_confirm))
# 手动添加数据
jl_list.append(("延边朝鲜族自治州",12))
jl_list.append(("白山市",52))
print(jl_list)
map = Map()
map.add("吉林省疫情分布",jl_list,"吉林")
map.set_global_opts(
    title_opts=TitleOpts(title="吉林疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"}
        ]
    )
)
map.render("吉林疫情地图.html")
"""