# -*- coding: cp936 -*-
from PIL import Image, ImageGrab
from pytesser import *
import time
from pymouse import PyMouse

m = PyMouse()

raw_input("���Ƚ�����ƶ�������λ�õ����Ͻ�,Ȼ���»س�.")
p1 = m.position()
print p1
raw_input("������������ƶ�������λ�õ����½�,Ȼ���»س�.")
p2 =  m.position()
print p2
print "�������λ�趨,��ʼ��ȡ���ݹ���."
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






