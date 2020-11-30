# -*- coding: utf-8 -*-
# @desc:

import math

from client.fractal import get_point_base_origin
from client.fractal.tools.draw_tools import draw_lines


def generate_snowflake(line_list, origin, length, angle, is_left=True):
    """
    绘制科赫雪花
    :param line_list:
    :param origin:
    :param length:
    :param angle:
    :param is_left:
    :return:
    """
    if length < 10:
        end = get_point_base_origin(origin, length, angle)
        line_list.append([origin, end])
    else:
        length /= 3
        generate_snowflake(line_list, origin, length, angle, is_left)
        end_fir = get_point_base_origin(origin, length, angle)

        if is_left:
            angle_change = -60
        else:
            angle_change = 60

        generate_snowflake(line_list, end_fir, length, angle + angle_change, is_left)
        end_sec = get_point_base_origin(end_fir, length, angle + angle_change)

        generate_snowflake(line_list, end_sec, length, angle - angle_change, is_left)
        end_trd = get_point_base_origin(end_sec, length, angle - angle_change)

        generate_snowflake(line_list, end_trd, length, angle, is_left)


if True:
    height = 1024
    width = 1024
    line_list = list()

    legth = int(width * 8 / 10)
    border_x = legth / 3
    border_y = legth / 20

    base_point1 = (border_y, border_x)
    base_point2 = (legth + border_y, border_x)
    base_point3 = (legth / 2 + border_y, border_x + int((math.sqrt(3.0) / 2) * legth))

    generate_snowflake(line_list,
                       origin=base_point1,
                       length=legth,
                       angle=0)

    generate_snowflake(line_list,
                       origin=base_point1,
                       length=legth,
                       angle=60.0,
                       is_left=False)

    generate_snowflake(line_list,
                       origin=base_point2,
                       length=legth,
                       angle=120.0)

    img_width = int(width * 1.0)
    img_height = int(height * 1.0)
    draw_lines(line_list, form=1024,
               name='snowflake',
               img_width=img_width, img_height=img_height,
               color=(0, 255, 0), line_width=2)
