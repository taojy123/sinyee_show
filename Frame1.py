# -*- coding: cp936 -*-
#Boa:Frame:Frame1

import wx
from PIL import Image, ImageGrab
from pytesser import *
import time
from pymouse import PyMouse
import threading
import traceback


global mself
global runflag


class ThreadClass1(threading.Thread):
    def run(self):
        global mself
        global runflag
        
        m = PyMouse()

        #raw_input("请先将鼠标移动到数据位置的左上角,然后按下回车.")
        wx.MessageBox("请不要点击该对话框的确定按钮\n先将鼠标移动到数据位置的左上角,然后按下回车...", "获取数据位置", wx.OK)
        p1 = m.position()
        print p1
        #raw_input("接下来将鼠标移动到数据位置的右下角,然后按下回车.")
        wx.MessageBox("接下来将鼠标移动到数据位置的右下角,然后按下回车...", "获取数据位置", wx.OK)
        p2 =  m.position()
        print p2
        print "完成数据位设定,开始获取数据工作."
        imbox = (p1[0], p1[1], p2[0], p2[1])

        prev_s = [0,0,0,0]
        while runflag:
            try:
                im = ImageGrab.grab(imbox)
                s = image_to_string(im)
                s = s.split()
                if s != prev_s and len(s)==4 :
                    sell =  float(s[0]) - float(prev_s[0])
                    buy = float(s[2]) - float(prev_s[2])
                    prev_s = s

                    print sell, buy
                    mself.staticText1.SetLabel(mself.staticText2.GetLabel())
                    mself.staticText2.SetLabel(mself.staticText3.GetLabel())
                    mself.staticText3.SetLabel(mself.staticText4.GetLabel())
                    mself.staticText4.SetLabel(mself.staticText5.GetLabel())
                    mself.staticText5.SetLabel(mself.staticText6.GetLabel())
                    mself.staticText6.SetLabel(mself.staticText7.GetLabel())
                    mself.staticText7.SetLabel(mself.staticText8.GetLabel())
                    mself.staticText8.SetLabel(mself.staticText9.GetLabel())
                    mself.staticText9.SetLabel(mself.staticText10.GetLabel())
                    mself.staticText10.SetLabel("%.1f"%sell)

                    mself.staticText11.SetLabel(mself.staticText12.GetLabel())
                    mself.staticText12.SetLabel(mself.staticText13.GetLabel())
                    mself.staticText13.SetLabel(mself.staticText14.GetLabel())
                    mself.staticText14.SetLabel(mself.staticText15.GetLabel())
                    mself.staticText15.SetLabel(mself.staticText16.GetLabel())
                    mself.staticText16.SetLabel(mself.staticText17.GetLabel())
                    mself.staticText17.SetLabel(mself.staticText18.GetLabel())
                    mself.staticText18.SetLabel(mself.staticText19.GetLabel())
                    mself.staticText19.SetLabel(mself.staticText20.GetLabel())
                    mself.staticText20.SetLabel("%.1f"%buy)

                im.save("show.jpg")
                pic=wx.Image("show.jpg")
                w,h = mself.staticBitmap1.GetSize()
                mself.staticBitmap1.SetBitmap(pic.Rescale(w,h).ConvertToBitmap())
            except:
                traceback.print_exc()
                wx.MessageBox("无法正常识别,请重新开始.注意数据截取位置.", "提醒", wx.OK)
                runflag = 0



def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1STATICBITMAP1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11, 
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT14, 
 wxID_FRAME1STATICTEXT15, wxID_FRAME1STATICTEXT16, wxID_FRAME1STATICTEXT17, 
 wxID_FRAME1STATICTEXT18, wxID_FRAME1STATICTEXT19, wxID_FRAME1STATICTEXT2, 
 wxID_FRAME1STATICTEXT20, wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, 
 wxID_FRAME1STATICTEXT5, wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, 
 wxID_FRAME1STATICTEXT8, wxID_FRAME1STATICTEXT9, 
] = [wx.NewId() for _init_ctrls in range(23)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(328, 253), size=wx.Size(746, 291),
              style=wx.DEFAULT_FRAME_STYLE, title='复盘数据监控系统')
        self.SetClientSize(wx.Size(730, 253))
        self.Bind(wx.EVT_CLOSE, self.OnFrame1Close)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(730, 253),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label='-',
              name='staticText1', parent=self.panel1, pos=wx.Point(32, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label='-',
              name='staticText2', parent=self.panel1, pos=wx.Point(96, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3, label='-',
              name='staticText3', parent=self.panel1, pos=wx.Point(160, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4, label='-',
              name='staticText4', parent=self.panel1, pos=wx.Point(224, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5, label='-',
              name='staticText5', parent=self.panel1, pos=wx.Point(288, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6, label='-',
              name='staticText6', parent=self.panel1, pos=wx.Point(352, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7, label='-',
              name='staticText7', parent=self.panel1, pos=wx.Point(416, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8, label='-',
              name='staticText8', parent=self.panel1, pos=wx.Point(480, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9, label='-',
              name='staticText9', parent=self.panel1, pos=wx.Point(552, 176),
              size=wx.Size(60, 14), style=0)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label='-', name='staticText10', parent=self.panel1,
              pos=wx.Point(624, 176), size=wx.Size(60, 14), style=0)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label='-', name='staticText11', parent=self.panel1,
              pos=wx.Point(32, 216), size=wx.Size(60, 14), style=0)

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label='-', name='staticText12', parent=self.panel1,
              pos=wx.Point(96, 216), size=wx.Size(60, 14), style=0)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label='-', name='staticText13', parent=self.panel1,
              pos=wx.Point(160, 216), size=wx.Size(60, 14), style=0)

        self.staticText14 = wx.StaticText(id=wxID_FRAME1STATICTEXT14,
              label='-', name='staticText14', parent=self.panel1,
              pos=wx.Point(224, 216), size=wx.Size(60, 14), style=0)

        self.staticText15 = wx.StaticText(id=wxID_FRAME1STATICTEXT15,
              label='-', name='staticText15', parent=self.panel1,
              pos=wx.Point(288, 216), size=wx.Size(60, 14), style=0)

        self.staticText16 = wx.StaticText(id=wxID_FRAME1STATICTEXT16,
              label='-', name='staticText16', parent=self.panel1,
              pos=wx.Point(352, 216), size=wx.Size(60, 14), style=0)

        self.staticText17 = wx.StaticText(id=wxID_FRAME1STATICTEXT17,
              label='-', name='staticText17', parent=self.panel1,
              pos=wx.Point(416, 216), size=wx.Size(60, 14), style=0)

        self.staticText18 = wx.StaticText(id=wxID_FRAME1STATICTEXT18,
              label='-', name='staticText18', parent=self.panel1,
              pos=wx.Point(480, 216), size=wx.Size(60, 14), style=0)

        self.staticText19 = wx.StaticText(id=wxID_FRAME1STATICTEXT19,
              label='-', name='staticText19', parent=self.panel1,
              pos=wx.Point(552, 216), size=wx.Size(60, 14), style=0)

        self.staticText20 = wx.StaticText(id=wxID_FRAME1STATICTEXT20,
              label='-', name='staticText20', parent=self.panel1,
              pos=wx.Point(624, 216), size=wx.Size(60, 14), style=0)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',
              parent=self.panel1, pos=wx.Point(192, 16), size=wx.Size(328, 128),
              style=0)

    def __init__(self, parent):
        global mself
        global runflag
        self._init_ctrls(parent)

        mself = self
        runflag = 1

        t = ThreadClass1()
        t.start()

    def OnFrame1Close(self, event):
        global runflag
        runflag = 0
        event.Skip()



