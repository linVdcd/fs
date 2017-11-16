# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Aug 18 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
from utils import *
import time

###########################################################################
## Class Mywin
###########################################################################

class Mywin(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"@wenxiang.zhang Tools", pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"人脸脸型识别工程工具包", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(
            wx.Font(20, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText1, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        m_radioBox1Choices = [u"获取图片文件列表", u"裁剪特定人脸区域", u"生成LMDB"]
        self.m_radioBox1 = wx.RadioBox(self, wx.ID_ANY, u"OPTIONS", wx.DefaultPosition, wx.DefaultSize,
                                       m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS)
        self.m_radioBox1.SetSelection(0)
        bSizer1.Add(self.m_radioBox1, 3, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        # self.m_radioBox1.Bind(wx.EVT_RADIOBOX, self.onRadioBox)  # 单选按钮框，事件绑定
        self.m_button1.Bind(wx.EVT_BUTTON, self.onClickButton)  # button事件

        self.SetSizer(bSizer1)
        self.Layout()

    def __del__(self):
        pass

    # 单选按钮事件
    def OnRadiogroup(self, e):
        rb = e.GetEventObject()

    def onRadioBox(self, e):
        print self.m_radioBox1.GetSelection(), self.m_radioBox1.GetStringSelection(), ' is clicked from Radio Box'

    def onClickButton(self, e):
        print self.m_radioBox1.GetStringSelection()
        option = self.m_radioBox1.GetSelection()
        if option == 0:
            dl = MyDialog1(self)
            dl.Show()
        elif option == 1:
            dl = MyDialog2(self)
            dl.Show()
        elif option == 2:
            dl = MyDialog3(self)
            dl.Show()
        else:
            print "请选择"



class MyDialog1(wx.Dialog):
    """
    制作图片文件列表对话框
    """
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"制作图片文件列表", pos=wx.DefaultPosition,
                           size=wx.Size(600, 150), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"图片文件目录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        bSizer11.Add(self.m_staticText11, 1, wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer11.Add(self.m_textCtrl11, 3, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_button11, 1, wx.ALL, 5)
        self.m_button11.Bind(wx.EVT_BUTTON, self.OnSelect)

        bSizer1.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"保存路径", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)
        bSizer12.Add(self.m_staticText12, 1, wx.ALL, 5)

        # wx.TextCtrl(parent, id, value, pos, size, style)
        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer12.Add(self.m_textCtrl12, 3, wx.ALL, 5)

        self.m_button12 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button12, 1, wx.ALL, 5)
        self.m_button12.Bind(wx.EVT_BUTTON, self.OnSave)

        bSizer1.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"是否要生成标签", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_checkBox1, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(self, wx.ID_ANY, u"开始生成", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button13, 0, wx.ALL, 5)
        self.m_button13.Bind(wx.EVT_BUTTON, self.GenerateFilelist)

        bSizer1.Add(bSizer13, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def OnSelect(self, e):
        wildcard = "Choose Images Directory"
        dlg = wx.DirDialog(None, 'Choose a directory: ',
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl11.SetValue(dlg.GetPath())

    def OnSave(self, e):
        dlg = wx.DirDialog(None, 'Choose a directory: ',
                              style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl12.SetValue(dlg.GetPath())


    def GenerateFilelist(self, e):
        image_path = self.m_textCtrl11.GetValue()
        label = self.m_checkBox1.GetValue()
        save_path = self.m_textCtrl12.GetValue()
        if image_path and save_path:
            util = Utils()
            util.makeFileListTxt(image_path, label, os.path.join(save_path, save_path))
        else:
            wx.MessageBox("请选择目录!", "Message", wx.OK | wx.ICON_INFORMATION)
        wx.MessageBox("生成完毕!", "Message", wx.OK | wx.ICON_INFORMATION)
        self.Destroy()


class MyDialog2(wx.Dialog):
    """
    裁剪人脸指定区域对话框
    """
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"裁剪指定人脸区域", pos=wx.DefaultPosition,
                           size=wx.Size(500, 200), style=wx.DEFAULT_DIALOG_STYLE)
        self.count = 50

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"图片列表文件(*.txt)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer3.Add(self.m_staticText2, 1, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY|wx.TE_READONLY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer3.Add(self.m_textCtrl1, 3, wx.ALL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button1, 1, wx.ALL, 5)
        self.m_button1.Bind(wx.EVT_BUTTON, self.OnSelectTxt)

        bSizer2.Add(bSizer3, 1, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"图片保存路径(目录)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer4.Add(self.m_staticText3, 1, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer4.Add(self.m_textCtrl2, 3, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_button2, 1, wx.ALL, 5)
        self.m_button2.Bind(wx.EVT_BUTTON, self.OnSaveDir)

        bSizer2.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"裁剪参数[left top right bottom]", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer5.Add(self.m_staticText4, 1, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, "0.05 0.15 0.05 0.08", wx.DefaultPosition, wx.DefaultSize)
        bSizer5.Add(self.m_textCtrl4, 4, wx.ALL, 5)
        bSizer2.Add(bSizer5, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"固定参数裁剪,请耐心等等...", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button3, 1, wx.ALL, 5)
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnCropFace)

        self.m_button4 = wx.Button(self, wx.ID_ANY, u"随机裁剪,请耐心等等...", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button4, 1, wx.ALL, 5)
        self.m_button4.Bind(wx.EVT_BUTTON, self.OnRandomCropFace)
        bSizer2.Add(bSizer6, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def OnSelectTxt(self, e):
        wildcard = "Text Files (*.txt)|*.txt"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, 0)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl1.SetValue(dlg.GetPath())

    def OnSaveDir(self, e):
        dlg = wx.DirDialog(None, 'Choose a directory: ',
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl2.SetValue(dlg.GetPath())

    def OnCropFace(self, e):
        file_list_txt = self.m_textCtrl1.GetValue()
        save_path = self.m_textCtrl2.GetValue()
        params = self.m_textCtrl4.GetValue()
        crop_params = [float(param) for param in params.split()]
        if file_list_txt and save_path:
            import getFrontFace
            getFrontFace.cropFace(file_list_txt, save_path, crop_params)
        # self.count = self.count + 1
        # self.m_gauge1.SetValue(self.count)
        wx.MessageBox("裁剪完成", "Message" ,wx.OK|wx.ICON_INFORMATION)
        self.Destroy()

    def OnRandomCropFace(self, e):
        file_list_txt = self.m_textCtrl1.GetValue()
        save_path = self.m_textCtrl2.GetValue()
        params = self.m_textCtrl4.GetValue()
        crop_params = [float(param) for param in params.split()]
        if file_list_txt and save_path:
            import getFrontFace
            getFrontFace.cropRandomFace(file_list_txt, save_path, crop_params)
        # self.count = self.count + 1
        # self.m_gauge1.SetValue(self.count)
        wx.MessageBox("裁剪完成", "Message" ,wx.OK | wx.ICON_INFORMATION)
        self.Destroy()


class MyDialog3(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(500, 270), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, u"caffe根目录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer6.Add(self.m_staticText10, 1, wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, "/home/leo/caffe", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer6.Add(self.m_textCtrl9, 3, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_button11, 0, wx.ALL, 5)
        self.m_button11.Bind(wx.EVT_BUTTON, self.OnSelectCaffeRoot)

        bSizer7.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"图片列表文件(*_label.txt)", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText5.Wrap(-1)
        bSizer8.Add(self.m_staticText5, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer8.Add(self.m_textCtrl4, 3, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.m_button5, 1, wx.ALL, 5)
        self.m_button5.Bind(wx.EVT_BUTTON, self.OnSelectTxt)

        bSizer7.Add(bSizer8, 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"图片所在目录", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer9.Add(self.m_staticText6, 1, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer9.Add(self.m_textCtrl5, 3, wx.ALL, 5)

        self.m_button51 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_button51, 0, wx.ALL, 5)
        self.m_button51.Bind(wx.EVT_BUTTON, self.OnImageDir)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"LMDB保存路径", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer10.Add(self.m_staticText7, 1, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        bSizer10.Add(self.m_textCtrl6, 3, wx.ALL, 5)

        self.m_button6 = wx.Button(self, wx.ID_ANY, u"选择", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.m_button6, 0, wx.ALL, 5)
        self.m_button6.Bind(wx.EVT_BUTTON, self.OnSaveDir)

        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"resize_width", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer11.Add(self.m_staticText8, 1, wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, '256', wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_textCtrl7, 2, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, u"resize_height", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        bSizer11.Add(self.m_staticText9, 1, wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, '256', wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.m_textCtrl8, 2, wx.ALL, 5)

        bSizer7.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.VERTICAL)

        self.m_button10 = wx.Button(self, wx.ID_ANY, u"开始生成", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_button10, 1, wx.ALL, 5)
        self.m_button10.Bind(wx.EVT_BUTTON, self.OnGenreateLMDB)

        bSizer7.Add(bSizer12, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

    def OnSelectCaffeRoot(self, e):
        dlg = wx.DirDialog(None, 'Choose a directory: ',
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl9.SetValue(dlg.GetPath())

    def OnSelectTxt(self, e):
        wildcard = "Text Files (*_label.txt)|*.txt"
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", wildcard, 0)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl4.SetValue(dlg.GetPath())

    def OnImageDir(self, e):
        dlg = wx.DirDialog(None, 'Choose a directory: ',
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl5.SetValue(dlg.GetPath())

    def OnSaveDir(self, e):
        dlg = wx.DirDialog(None, 'Choose a directory: ',
                           style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dlg.ShowModal() == wx.ID_OK:
            self.m_textCtrl6.SetValue(dlg.GetPath())

    def OnGenreateLMDB(self, e):
        caffe_root = self.m_textCtrl9.GetValue()
        file_list_txt = self.m_textCtrl4.GetValue()
        image_dir = self.m_textCtrl5.GetValue()
        save_path = self.m_textCtrl6.GetValue()
        s_width = self.m_textCtrl7.GetValue()
        s_height = self.m_textCtrl8.GetValue()
        try:
            width = int(s_width)
            height = int(s_height)
            if file_list_txt and save_path and image_dir:
                util = Utils()
                util.createLMDB(caffe_root, file_list_txt, image_dir, save_path, width, height)
            wx.MessageBox("转换完成", "Message", wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        except:
            wx.MessageBox("请输入有效的Width和height", "Error", wx.OK | wx.ICON_ERROR)


if __name__ == '__main__':
    app = wx.App()
    window = Mywin(None)
    panel = MyPanel1(window)
    window.Show()
    app.MainLoop()
