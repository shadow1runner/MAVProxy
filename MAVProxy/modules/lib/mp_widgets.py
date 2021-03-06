#!/usr/bin/env python
'''
some useful wx widgets

Andrew Tridgell
June 2012
'''

from wx_loader import wx
import cv2
import numpy as np

class ImagePanel(wx.Panel):
    '''a resizable panel containing an image'''
    def __init__(self, parent, img):
        wx.Panel.__init__(self, parent, -1, size=(1, 1))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.set_image(img)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_paint(self, event):
        '''repaint the image'''
        dc = wx.AutoBufferedPaintDC(self)
        dc.DrawBitmap(self._bmp, 0, 0)

    def set_image(self, img):
        '''set the image to be displayed'''
        self._bmp = wx.BitmapFromBuffer(img.shape[1], img.shape[0], np.uint8(img)) # http://stackoverflow.com/a/16866833/2559632
        self.SetMinSize((self._bmp.GetWidth(), self._bmp.GetHeight()))
