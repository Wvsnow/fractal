# -*- coding: utf-8 -*-
# @desc:   Ref  https://blog.csdn.net/weixin_28710515/article/details/90735967


def iterator(c, r, max_iter):
    # 定义逃逸时间函数，c为初始值，r为收敛半径，max_iter为最大迭代次数，返回逃逸时间
    z = c  # 初始值
    for iter in range(0, max_iter, 1):
        if abs(z) > r:
            break
        z = z ** 2 + c
    return iter


def plot_mandelbrot():  # 定义绘制mandelbrot图像
    X = np.linspace(-1.75, 1.05, 5000)  # 实部范围，5000这个数要量力而行
    Y = np.linspace(-1.25, 1.25, 5000)  # 虚部范围，5000这个数要量力而行
    real, image = np.meshgrid(X, Y)  # 生成网格点坐标矩阵。
    c = real + image * 1j  # 构造复数
    mandelbrot_set = np.frompyfunc(iterator, 3, 1)(c, 1.5, 100).astype(np.float)
    # frompyfunc(func, nin, nout)，其中func是需要转换的函数，nin是函数的输入参数的个数，nout是此函数的返回值的个数,frompyfunc把Python里的函数（可以是自写的）转化成ufunc


import numpy as np
from PIL import Image
import time


def mandelbrot(c, maxiter):
    z = c
    for n in range(maxiter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return 0


def mandelbrot_set(xmin, xmax, ymin, ymax, img, maxiter):
    width, height = img.size[0], img.size[1]
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)

    [img.putpixel((idx1, idx2),
                  (mandelbrot(complex(r, i), maxiter) << 21) + (mandelbrot(complex(r, i), maxiter) << 10)
                  + mandelbrot(complex(r, i), maxiter) * 8) for idx1, r in enumerate(r1) for idx2, i in enumerate(r2)]


bitmap = Image.new("RGB", (1024, 1024), "white")

start = time.time()
mandelbrot_set(-2.0, 0.5, -1.25, 1.25, bitmap, 100)  # prime paras
# mandelbrot_set(-2.0, - 0.75, -0.625, 0.625, bitmap, 100)
# mandelbrot_set(-2.0, - 1.9, -0.05, 0.05, bitmap, 100)

print("Time cost {} seconds".format(round(time.time() - start, 2)))

bitmap.show()
