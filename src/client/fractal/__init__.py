# -*- coding: utf-8 -*-

import math
import datetime
import random


def get_divide_pnt(s_pnt, t_pnt, div=0.5):
    return (
        s_pnt[0] * (1 - div) + t_pnt[0] * div,
        s_pnt[1] * (1 - div) + t_pnt[1] * div
    )


def get_point_base_origin(origin, length, angle):
    x, y = origin
    angle *= math.pi / 180
    x += length * math.cos(angle)
    y += length * math.sin(angle)
    return x, y


def get_point_based_start(origin, length, angle):
    """
    基于起点坐标，根据向量（长度、角度）获取终点坐标
    :param origin:
    :param length:
    :param angle:
    :return:
    """
    x, y = origin
    angle *= math.pi / 180
    x += length * math.cos(angle)
    y += length * math.sin(angle)
    return x, y
