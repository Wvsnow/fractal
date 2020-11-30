# -*- coding: utf-8 -*-
# @desc:

import random
from client.fractal import get_divide_pnt
from client.fractal.tools.draw_tools import draw_points


def sierpinski(points, degree):
    """
    sierpinski 三角形
    随机因素，确定结果
    ref : https://zhuanlan.zhihu.com/p/24318397
    :param points:  points = [(-500, -350), (0, 400), (500, -350)]
    :param degree:  迭代次数
    :return:
    """
    i = 0
    result = list()
    print(points)

    r1 = random.randint(1, 999999)
    r2 = random.randint(1, 999999)
    r3 = random.randint(1, 999999)
    r_sum = r1 + r2 + r3
    start_pnt = (
        points[0][0] * (r1 / r_sum) + points[1][0] * (r2 / r_sum) + points[2][0] * (r3 / r_sum),
        points[0][1] * (r1 / r_sum) + points[1][1] * (r2 / r_sum) + points[2][1] * (r3 / r_sum)
    )
    print(start_pnt)
    result.append(start_pnt)

    while i < degree:
        rnum = random.randint(0, 999999)
        rnum_mod = rnum % 3

        next_pnt = get_divide_pnt(points[rnum_mod], result[i])
        result.append(next_pnt)

        i = i + 1
    return result


if False:
    points = [(0.0, 0.0), (0.0, 20000.0), (14000.0, 10000.0)]
    points = [(0.0, 0.0), (0.0, 20000.0), (20000.0, 10000.0)]
    degree = 100000
    points_all = sierpinski(points, degree)

    _draw_points(points_all, 20000.0, 'sierpinski')

if True:
    points = [(0.0, 10000.0), (0.0, 20000.0), (20000.0, 20.0)]
    degree = 100000
    points_all = sierpinski(points, degree)

    draw_points(points_all, 20000.0, 'sierpinski')

