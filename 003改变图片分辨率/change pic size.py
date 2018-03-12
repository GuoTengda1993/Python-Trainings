# -*- coding:utf-8 -*-
import os
import re
from PIL import Image


dir = r'C:\Users\pc\Desktop\Python Training\003改变图片分辨率'
file_list = os.listdir(dir)
jpg_list = []
for file in file_list:
    if re.match('\w+?.jpg', file):
        jpg_list.append(file)
    else:
        pass
n = 0
for each in jpg_list:
    n +=1
    name = str(n) + '.jpg'
    img = Image.open(str(each))
    w, h = img.size
    if w > 640:
        h1 = int(640*h/w)
        new_img = img.resize((640, h1))
    elif h > 1136:
        w1 = int(1136*w/h)
        new_img = img.resize((w1, 1136))
    new_img.save(name, 'jpeg')
