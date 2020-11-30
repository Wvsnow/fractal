# -*- coding: utf-8 -*-


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import datetime


def draw_points(points_list, form, name, img_width=1024, img_height=1024, color=(255, 0, 0)):
    image = Image.new('RGB', (img_width, img_height), (255, 255, 255))
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(img_width):
        for y in range(img_height):
            draw.point((x, y), fill=(255, 255, 255))

    for item in points_list:
        draw.point((img_width * item[0] / form, img_height * item[1] / form), fill=color)

    # 模糊:
    time = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    path_prefix = '/tmp/apps/fractal/imgs/'
    file_name = 'F_' + name + '_D' + str(len(points_list)) + '_T' + time + '.jpg'
    full_file_path = path_prefix + file_name
    image.save(full_file_path, 'jpeg')
    # image.close()

    print("""
    -- ------------------------------------------
    -- Drawing image based on points has been done
    -- save path is: {dir_name} 
    -- ------------------------------------------
    """.format(dir_name=full_file_path))


def draw_lines(line_list, form, name, img_width=1024, img_height=1024, color=(255, 0, 0), line_width=1):
    image = Image.new('RGB', (img_width, img_height), (255, 255, 255))
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(img_width):
        for y in range(img_height):
            draw.point((x, y), fill=(255, 255, 255))

    for item in line_list:
        # draw.line([(0, 0), (255, 500)], fill=12, width=2, joint=None)
        draw.line([item[0], item[1]], fill=item[2] if len(item) > 2 else color, width=line_width, joint=None)

    time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    path_prefix = '/tmp/apps/fractal/imgs/'
    file_name = 'F_' + name + '_D' + str(len(line_list)) + '_T' + time + '.jpg'
    full_file_path = path_prefix + file_name
    image.save(full_file_path, 'jpeg')
    # image.close()

    print("""
        -- ------------------------------------------
        -- Drawing image based on lines has been done
        -- save path is: {dir_name} 
        -- ------------------------------------------
        """.format(dir_name=full_file_path))

