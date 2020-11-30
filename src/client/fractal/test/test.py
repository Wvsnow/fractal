# -*- coding: utf-8 -*-
# @desc:

# -------------------------------------------------------

from PIL import Image
from client.fractal import get_divide_pnt

from client.fractal.tools.draw_tools import draw_points

try:
    im = Image.open("test.jpg")
    n_im = Image.new("RGB", (128, 128), "#FF0000")
    n_im.show()
except Exception as e:
    print(e)

# -------------------------------------------------------
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime
import random


# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def test_img_gen_001():
    # 240 x 60:
    width = 1024
    height = 1024
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('Arial.ttf', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(255, 255, 255))
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    time = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    path_prefix = '../../resources/imgs/'
    file_name = 'code-' + time + '.jpg'
    full_file_path = path_prefix + file_name
    image.save(full_file_path, 'jpeg')


# 康托集
def _my_conto():
    width = 1024
    height = 1024
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(255, 255, 255))

    draw.line([(0, 0), (255, 500)], fill=12, width=2, joint=None)

    len0 = 1000  # 初始线条长度
    leni = len0  # 当前最小线条长度
    line = 0  # 当前行数

    while leni > 1:
        n = 2 ** line  # 集合元素份数
        tep = [0, ]  # 元素第一个端点位置
        while len(tep) < n:
            nt = (tep[-1] + leni) * 2  # 接下来首个元素位置
            tepp = []  # 接下来元素位置
            for j in tep:
                tepp.append(nt + j)
            tep.extend(tepp)
        for k in tep:
            draw.line([(k, 30 * line + 5), (k + leni, 30 * line + 5)])
        line += 1
        leni = leni / 3

    # 模糊:
    time = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    path_prefix = '../../resources/imgs/'
    file_name = 'fractal-' + time + '.jpg'
    full_file_path = path_prefix + file_name
    image.save(full_file_path, 'jpeg')


def sierpinski(points, degree):
    """
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


if True:
    points = [(0.0, 0.0), (0.0, 20000.0), (14000.0, 10000.0)]
    points = [(0.0, 0.0), (0.0, 20000.0), (20000.0, 10000.0)]
    degree = 100000
    points_all = sierpinski(points, degree)

    draw_points(points_all, 20000.0, 'sierpinski')

if False:
    points = [(0.0, 10000.0), (0.0, 20000.0), (20000.0, 20.0)]
    degree = 100000
    points_all = sierpinski(points, degree)

    draw_points(points_all, 20000.0, 'sierpinski')
