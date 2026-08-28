import numpy
import pandas
from spsspro.algorithm import supervised_learning

# 生成案例数据
data_x = pandas.DataFrame({
    "A": numpy.random.random(size=100),
    "B": numpy.random.random(size=100)
})
data_y = pandas.Series(data=numpy.random.random(size=100), name="C")

# adaboost回归，输入参数详细可以光标放置函数括号内按shift+tab查看，输出结果参考spsspro模板分析报告
result = supervised_learning.adaboost_regression(data_x=data_x, data_y=data_y)
print(result)
