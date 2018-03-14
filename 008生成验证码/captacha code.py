# -*- coding: utf-8 -*-
# 参考廖雪峰大神的博客：
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


char_list = []
for i in range(97, 123):
    char_list.append(chr(i))
for i in range(65, 91):
    char_list.append(chr(i))
for i in range(48, 58):
    char_list.append(chr(i))


def random_char():
    global char_list
    return random.choice(char_list)


def random_color():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def random_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('arial.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=random_color())

for t in range(4):
    draw.text((60*t+10, 10), random_char(), font=font, fill=random_color2())

image = image.filter(ImageFilter.BLUR)
image.save('captcha.jpg', 'jpeg')
