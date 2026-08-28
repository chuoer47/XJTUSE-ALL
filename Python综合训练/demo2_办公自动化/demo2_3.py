from pyecharts import options as opts
from pyecharts.charts import Map

quxian = ['广东省', '云岩区', '南明区', '花溪区', '乌当区', '白云区', '修文县', '息烽县', '开阳县', '清镇市']
values3 = [3, 5, 7, 8, 2, 4, 7, 8, 2, 4]

c = (
    Map()
        .add("商家A", [list(z) for z   in zip(quxian, values3)], "西安")
        .set_global_opts(title_opts=opts.TitleOpts(title="Map-基本示例"), visualmap_opts=opts.VisualMapOpts())
        .render("map_visualmap_piecewise.html")
)
