# -*- coding: utf-8 -*-
# @desc:

from matplotlib import pyplot

from numpy import array
from numpy.random import normal


def getData():
    heights = []
    weights = []
    books = []
    N = 10000
    for i in range(N):
        while True:
            # 身高服从均值为172，标准差为6的正态分布
            height = normal(172, 6)
            if 0 < height:
                break
        while True:
            # 体重由身高作为自变量的线性回归模型产生，误差服从标准正态分布
            weight = (height - 80) * 0.7 + normal(0, 1)
            if 0 < weight:
                break
        while True:
            # 借阅量服从均值为20，标准差为5的正态分布
            number = normal(20, 5)
            if 0 <= number and number <= 50:
                book = 'E' if number < 10 else (
                    'D' if number < 15 else ('C' if number < 20 else ('B' if number < 25 else 'A')))
                break
        heights.append(height)
        weights.append(weight)
        books.append(book)
    return array(heights), array(weights), array(books)


def drawPie(books):
    labels = ['A', 'B', 'C', 'D', 'E']
    bookGroup = {}
    for book in books:
        bookGroup[book] = bookGroup.get(book, 0) + 1
    # 创建饼形图
    # 第一个参数是扇形的面积
    # labels参数为扇形的说明文字
    # autopct参数为扇形占比的显示格式
    pyplot.pie([bookGroup.get(label, 0) for label in labels], labels=labels, autopct='%1.1f%%')
    pyplot.title("Number of Books Students Read")
    pyplot.show()


heights, weights, books = getData()

drawPie(books)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# 通过加载sns自带数据库中的数据（具体数据可以不关心）
flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

# 使用每个单元格中的数据值绘制一个热力图heatmap
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5)
plt.show()
