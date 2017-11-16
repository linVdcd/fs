# -*- coding: utf-8 -*-

from __future__ import division
import os
import sys

class Utils():
    def __init__(self):
        self.globalFilelist = []

    def getFileList(self, imagerootpath, label):
        """
        获取图片文件列表
        :param imagerootpath: 图片文件目录
        :param label: 是否添加标签
        :return: 图片文件列表
        """
        if not os.path.isdir(imagerootpath):
            ext = imagerootpath.split('.')[-1]  # 判断是否是图片
            if ext in ['jpg', 'png', 'bmp']:
                if label:
                    if sys.platform == 'linux2':
                        line = imagerootpath + ' ' + imagerootpath.split('/')[-2] + '\n'
                    else:
                        line = imagerootpath + ' ' + imagerootpath.split('\\')[-2] + '\n'
                else:
                    line = imagerootpath + '\n'
                self.globalFilelist.append(line)
        else:
            paths = os.listdir(imagerootpath)
            for path in paths:
                self.getFileList(os.path.join(imagerootpath, path), label)

    def makeFileListTxt(self, imagerootpath, label, savefilepath):
        """
        将图片文件列表写入文本文件
        :param imagerootpath: 图片文件目录
        :param label: 是否添加标签
        :param savefilepath: 文件保存路径
        :return:
        """
        if label:
            savefilename = savefilepath+"/"+imagerootpath.split("/")[-1]+"_label.txt"
        else:
            savefilename = savefilepath+"/"+imagerootpath.split("/")[-1]+".txt"

        self.getFileList(imagerootpath, label=label)
        with open(savefilename, 'w') as fw:
            for image_path in self.globalFilelist:
                fw.write(image_path)
        print "文件列表", savefilename, "生成完毕"

    def createLMDB(self, caffe_root, file_list, images_path, lmdb_path, resize_height, resize_width):
        print caffe_root, file_list, images_path, lmdb_path, resize_height, resize_width
        new_file_list = "./temp.txt"
        with open(new_file_list, 'w+') as fn:
            for line in open(file_list):
                new_line = line.replace(images_path+"/", '')
                fn.write(new_line)
        lmdb_name = os.path.split(images_path)[-1]+"_"+str(resize_width)+"_lmdb"
        cmd = "sh utils/create_lmdb.sh %s %s %s %s %s %s %s" % (caffe_root, new_file_list, images_path, lmdb_path, lmdb_name, resize_height, resize_width)
        os.system(cmd)
