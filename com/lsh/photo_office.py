# -*- coding: utf-8 -*-
# @Time : 2020/4/23 16:21
# @Author : LSH
# @Desc : 
# @Version : 1.0.0

from  PIL import Image

img = Image.open('./res/guido.jpg')
rect = 80, 20, 310, 360

img.crop(rect).show