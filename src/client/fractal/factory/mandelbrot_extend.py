# -*- coding: utf-8 -*-
# @desc:

import numpy as np

import random
from client.fractal import get_divide_pnt
from client.fractal.tools.draw_tools import draw_points


def getEscapeTime(c):
    "计算参数c的逃逸时间，该逃逸时间将用作点的颜色"
    z = 0
    for i in range(100):
        if abs(z) > 2:
            return i
        z = z * z + c
    return i


def computeMandelbrot(xCenter, yCenter, semiWidth, N):
    xFrom, xTo, yFrom, yTo = xCenter - semiWidth, xCenter + semiWidth, \
                             yCenter - semiWidth, yCenter + semiWidth
    y, x = np.ogrid[yFrom:yTo:N * 1j, xFrom:xTo:N * 1j]
    c = x + y * 1j
    print("c.shape:", c.shape, "x.shape:", x.shape, "y.shape:", y.shape)
    return np.frompyfunc(getEscapeTime, 1, 1)(c).astype(np.float)


def drawMandelbrot(ax, xCenter, yCenter, semiWidth, N, cmap):
    "(xCenter,yCenter)-中心点，semiWidth-矩形半宽，N*N像素."
    ax.set_axis_off()
    ds = computeMandelbrot(xCenter, yCenter, semiWidth, N)
    ax.imshow(ds, cmap=cmap)  # 在子图-ax上绘制图像，ds是计算而得的二维数组，其元素为逃逸时间


from matplotlib import cm


def refresh():
    c = cm.get_cmap(para.cmaps[para.idxColorMap % len(para.cmaps)])
    drawMandelbrot(para.ax0, para.x, para.y, semiWidth=0.2, N=1024, cmap=c)
    drawMandelbrot(para.ax1, para.x, para.y, semiWidth=0.2 ** 3, N=1024, cmap=c)
    # drawMandelbrot(para.ax0, para.x, para.y, semiWidth=0.05, N=1024, cmap=c)
    # drawMandelbrot(para.ax1, para.x, para.y, semiWidth=0.05 ** 2, N=1024, cmap=c)
    para.fig.canvas.draw()  # 要求图-Fig重绘


from matplotlib import pyplot as plt


def on_key_release(event):  # 按键松开勾子函数
    if event.key == 'up':
        para.idxColorMap += 1
    elif event.key == 'down':
        para.idxColorMap -= 1
    else:
        return
    refresh()


class Para:  # 一个仅有名字的Para类用于存储全局参数
    pass


para = Para()
# para.x, para.y = 0.27322626, 0.595153338   # Prime paras
para.x, para.y = 0.27322626, 0.595153338
para.idxColorMap = 0
para.cmaps = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
              'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow',
              'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
para.fig = plt.figure(figsize=(12, 6), dpi=800)
para.fig.canvas.mpl_connect('key_release_event', on_key_release)
plt.subplots_adjust(0, 0, 1, 1, 0.0, 0)
para.ax0 = plt.subplot(121)
para.ax1 = plt.subplot(122)
refresh()
plt.show()
