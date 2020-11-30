# -*- coding: utf-8 -*-
# @desc:

import sys
import math

from client.fractal import get_point_based_start, get_point_base_origin
from client.fractal.tools.draw_tools import draw_lines

def generate_binary_tree_lines(line_list, origin, length, angle, scale,
                               left_angle, left_scale, right_angle, right_scale):
    """
    二叉树生成
    :param line_list:
    :param origin:
    :param length:
    :param angle:
    :param scale:
    :param left_angle:
    :param left_scale:
    :param right_angle:
    :param right_scale:
    :return:
    """
    if length < 2:
        return  # 当length小于2的时候，停止画线(也可以用下面两行代码，表示当length小于2的时候，再画一次停止)
    else:
        end = get_point_base_origin(origin, length * scale, angle)
        line_list.append([origin, end])

        generate_binary_tree_lines(line_list, end, length * left_scale, angle + left_angle, scale,
                                   left_angle, left_scale, right_angle, right_scale)
        generate_binary_tree_lines(line_list, end, length * right_scale, angle + right_angle, scale,
                                   left_angle, left_scale, right_angle, right_scale)


if True:
    height = 1024
    width = 1024
    line_list = list()

    generate_binary_tree_lines(line_list,
                               origin=(width / 2, height), length=height,
                               angle=-90, scale=0.4,
                               left_angle=-40, left_scale=0.55,
                               right_angle=30, right_scale=0.65)

    img_width = int(width * 1.5)
    img_height = int(height * 1.2)
    draw_lines(line_list, form=15000,
               name='binary_tree',
               img_width=img_width, img_height=img_height,
               color=(0, 255, 0), line_width=2)


def generate_tree_lines(line_list, origin, length, angle, angle_delta, scale, left_angle, left_scale, right_angle,
                        right_scale):
    """
    三叉树生成
    树状结构生成，蕨类植物叶子形状
    :param line_list:  计算结果线段集合
    :param origin:     基准点
    :param length:
    :param angle:
    :param angle_delta:
    :param scale:
    :param left_angle:
    :param left_scale:
    :param right_angle:
    :param right_scale:
    :return:
    """
    if length < 4:
        return  # 当length小于2的时候，停止画线(也可以用下面两行代码，表示当length小于2的时候，再画一次停止)

    else:
        end = get_point_based_start(origin, length * scale, angle)
        line_list.append([origin, end])

        generate_tree_lines(line_list, end, length * left_scale, angle + left_angle, angle_delta, scale,
                            left_angle, left_scale, right_angle, right_scale)
        generate_tree_lines(line_list, end, (1 - scale) * length, angle - angle_delta, angle_delta, scale,
                            left_angle, left_scale, right_angle, right_scale)
        generate_tree_lines(line_list, end, length * right_scale, angle + right_angle, angle_delta, scale,
                            left_angle, left_scale, right_angle, right_scale)


if True:
    height = 1024 * 2
    width = 1024 * 2
    line_list = list()
    # generate_tree_lines(line_list,
    #                     origin=(width / 2, height), length=height,
    #                     angle=-90, angle_delta=10, scale=0.2,
    #                     left_angle=-40, left_scale=0.3,
    #                     right_angle=30, right_scale=0.3)
    generate_tree_lines(line_list,
                        origin=(width / 2, height), length=height,
                        angle=-90, angle_delta=12, scale=0.2,
                        left_angle=-40, left_scale=0.3,
                        right_angle=30, right_scale=0.3)

    draw_lines(line_list, form=10000,
               name='fern',
               img_width=width, img_height=height,
               color=(0, 255, 0), line_width=2)

