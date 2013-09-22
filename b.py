# -*- coding: cp936 -*-
from PIL import Image, ImageGrab
from pytesser import *
import time
from pymouse import PyMouse

m = PyMouse()

raw_input("请先将鼠标移动到数据位置的左上角,然后按下回车.")
p1 = m.position()
print p1
raw_input("接下来将鼠标移动到数据位置的右下角,然后按下回车.")
p2 =  m.position()
print p2
print "完成数据位设定,开始获取数据工作."
imbox = (p1[0], p1[1], p2[0], p2[1])


#print image_file_to_string('1.jpg')
prev_s = [0,0,0,0]
while True:
    im = ImageGrab.grab(imbox)
    s = image_to_string(im)
    s = s.split()
    if s != prev_s and len(s)==4 :
        sell =  float(s[0]) - float(prev_s[0])
        buy = float(s[2]) - float(prev_s[2])
        print sell, buy
        prev_s = s
        
    im.save("a.jpg")






