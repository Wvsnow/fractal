# -*- coding: utf-8 -*-
# @desc:


import pygame


# 康托集
def _my_conto():
    pygame.init()
    screen = pygame.display.set_caption('康托集')
    screen = pygame.display.set_mode([1000, 250])
    screen.fill([255, 255, 255])
    pygame.display.flip()

    len0 = 1000  # 初始线条长度
    leni = len0  # 当前最小线条长度
    line = 0  # 当前行数

    while leni > 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        n = 2 ** line  # 集合元素份数
        tep = [0, ]  # 元素第一个端点位置
        while len(tep) < n:
            nt = (tep[-1] + leni) * 2  # 接下来首个元素位置
            tepp = []  # 接下来元素位置
            for j in tep:
                tepp.append(nt + j)
            tep.extend(tepp)
        for k in tep:
            pygame.draw.line(screen, [0, 0, 0], [
                k, 30 * line + 5], [k + leni, 30 * line + 5], 10)
        pygame.display.flip()
        line += 1
        leni = leni / 3

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


# 谢尔宾斯基方毯
def _my_square():
    def p2(p, r, d):
        # p: 参考左上顶点
        # r: 距离参考点向右偏移距离
        # d: 距离参考点向下偏离距离
        return [p[0] + r, p[1] + d]

    def points(p, leni):
        # 返回p,leni对应的四边形四个顶点列表
        return [p, p2(p, leni, 0), p2(p, leni, leni), p2(p, 0, leni)]

    def draw(p, leni):
        # p：左上顶点
        # leni：边长
        leni /= 3
        pygame.draw.polygon(screen, [255, 255, 255],
                            points(p2(p, leni, leni), leni))
        if leni > 3:
            draw(p, leni)
            draw(p2(p, leni, 0), leni)
            draw(p2(p, 2 * leni, 0), leni)

            draw(p2(p, 0, leni), leni)
            draw(p2(p, 2 * leni, leni), leni)

            draw(p2(p, 0, 2 * leni), leni)
            draw(p2(p, leni, 2 * leni), leni)
            draw(p2(p, 2 * leni, 2 * leni), leni)
            pygame.display.flip()

    maxlen = 500  # 边界

    pygame.init()
    screen = pygame.display.set_caption(u'谢尔宾斯基方毯')
    screen = pygame.display.set_mode([maxlen, maxlen])
    screen.fill([0, 0, 0])
    pygame.display.flip()

    draw([0, 0], maxlen)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()


# 谢尔宾斯基三角垫
def _my_triangle():
    def mid(a, b):
        # 求出a, b点的中点坐标
        return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]

    def draw(one, two, tri):
        # 参数代表三个顶点,上、左、右排序
        if one[0] - two[0] > 2:  # 可分
            draw(one, mid(one, two), mid(one, tri))  # 画上面的三角
            draw(mid(one, two), two, mid(two, tri))  # 画左边三角
            draw(mid(one, tri), mid(two, tri), tri)  # 画右边的三角
            pygame.display.flip()
        else:  # 达到最小结构
            pygame.draw.polygon(screen, [0, 0, 0], [one, two, tri])

    maxlen = 500  # 边界

    pygame.init()
    screen = pygame.display.set_caption(u'谢尔宾斯基三角垫')
    screen = pygame.display.set_mode([maxlen, maxlen])
    screen.fill([255, 255, 255])
    pygame.display.flip()

    draw([maxlen / 2, 0], [0, maxlen], [maxlen, maxlen])
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()




_my_triangle()