# -*- coding: utf-8 -*-
from __future__ import division
import os
import sys
import cv2
import numpy as np
import shutil
from predict import Predict
from multiprocessing import Pool

file_list = []  # 文件列表，全局变量
predictor = None
net = None
transformer = None


def makefilelist(imagerootpath, label):
    """
    制作文件图片文件列表
    :param imagerootpath:图片所在根目录
    :param label:如果为True,则添加图片所在目录的名称作为label
    :return:
    """
    global file_list
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
            file_list.append(line)
    else:
        paths = os.listdir(imagerootpath)
        for path in paths:
            makefilelist(os.path.join(imagerootpath, path), label)


# test makefilelist
def test_makefilelist(path):
    makefilelist(path, label=True)


def cropFace(image_path, detector, save_path, rescale, no_face_images_dir, multiface_images_dir):
    image_path = image_path.strip('\n')
    if not os.path.exists(image_path):
        print '>', image_path, 'does not exist!'
        return
    print '> crop', image_path
    label, img_name = image_path.split('/')[-2:]
    img = cv2.imread(image_path.strip('\n'), cv2.IMREAD_COLOR)
    dets = detector(img, 1)

    if len(dets) == 0:
        print '>', img_name, '检测不到人脸，跳过该张图片！'
        shutil.copy(image_path, os.path.join(no_face_images_dir, img_name))
        return
    if len(dets) > 1:
        print '> 理检测到不止一张脸，只裁剪第一张脸 ！'
        shutil.copy(image_path, os.path.join(multiface_images_dir, img_name))
    else:
        detected_face = dets[0]
        imgcrop = cropImg(img, detected_face.left(), detected_face.top(),\
                          detected_face.right(), detected_face.bottom(), rescale)
        croped_save_path = os.path.join(save_path, label)
        if not os.path.exists(croped_save_path):
            os.makedirs(croped_save_path)
        cv2.imwrite(os.path.join(croped_save_path, img_name), imgcrop)

def getCropFace(image_path, detector, rescale):
    image_path = image_path.strip('\n')
    if not os.path.exists(image_path):
        print '>', image_path, 'does not exist!'
        return
    print '> crop', image_path
    label, img_name = image_path.split('/')[-2:]
    img = cv2.imread(image_path.strip('\n'), cv2.IMREAD_COLOR)
    dets = detector(img, 1)

    if len(dets) == 0:
        print '>', img_name, '检测不到人脸，跳过该张图片！'
        return None
    if len(dets) > 1:
        print '> 理检测到不止一张脸，只裁剪第一张脸 ！'
    detected_face = dets[0]
    imgcrop = cropImg(img, detected_face.left(), detected_face.top(),\
                      detected_face.right(), detected_face.bottom(), rescale)
    return imgcrop


def cropImg(img, tlx, tly, brx, bry, rescale):
    l = float(tlx)
    t = float(tly)
    ww = float(brx - l)
    hh = float(bry - t)

    # Approximate LM tight BB
    h = img.shape[0]
    w = img.shape[1]
    cx = l + ww/2
    cy = t + hh/2
    tsize = max(ww, hh)/2
    # l = cx - tsize
    # t = cy - tsize

    # Approximate expanded bounding box
    bl = int(round(cx - rescale[0]*tsize))
    bt = int(round(cy - rescale[1]*tsize))
    br = int(round(cx + rescale[2]*tsize))
    bb = int(round(cy + rescale[3]*tsize))
    nw = int(br - bl)
    nh = int(bb - bt)
    imcrop = np.zeros((nh, nw, 3), dtype='uint8')

    ll = 0
    if bl < 0:
        ll = -bl
        bl = 0
    rr = nw
    if br > w:
        rr = w+nw - br
        br = w
    tt = 0
    if bt < 0:
        tt = -bt
        bt = 0
    bbb = nh
    if bb > h:
        bbb = h+nh - bb
        bb = h
    imcrop[tt:bbb, ll:rr, :] = img[bt:bb, bl:br, :]
    return imcrop


def predict(image_path, deploy_file, model_file):
    predictor = Predict(deploy_file, model_file)
    net = predictor.load_model()
    transformer = predictor.get_transformer(net)
    order = predictor.predict(image_path, net, transformer)
    return order


def get_accuracy(filelist, deploy_file, model_file):
    counts = 0
    errors = 0
    predictor = Predict(deploy_file, model_file)
    net = predictor.load_model()
    transformer = predictor.get_transformer(net)

    for line in open(filelist):
        line = line.strip('\n')
        name_label = line.split(' ')
        if len(name_label) != 2:
            continue
        counts += 1
        name, label = name_label
        order = predictor.predict(name, net, transformer)
        if str(order) != str(label):
            errors += 1
            print name, 'label:', label, 'order:', order, 'error number:', errors
    return 1 - errors/counts

global_list = []  # 保存分类结果


def classify(image_path):
    global nums
    order = predictor.predict(image_path, net, transformer)
    record = image_path+' '+str(order) + '\n'
    print record
    return record


def get_result(record):
    global_list.append(record)


def classify_photos(filelist, deploy_file, model_file):
    global predictor
    global net
    global transformer
    predictor = Predict(deploy_file, model_file)
    net = predictor.load_model()
    transformer = predictor.get_transformer(net)
    # for line in open(filelist):
    #     classify(line.strip('\n'))
    pool = Pool(processes=5)
    for line in open(filelist):
        pool.apply_async(classify, (line.strip('\n'),), callback=get_result)
    pool.close()
    pool.join()
    print 'end'

import re
def parse_log(log_file):
    iteration = []
    accuracy = []
    p_test = re.compile(r"^I(?:.*)Iteration\s+(?P<iteration>\d+),\s+Testing.*")
    p_test2 = re.compile(r"^I(?:.*Test net output.*accuracy = )(?P<accuracy>[\d|\.]+)")
    for line in open(log_file):
        m1 = re.match(p_test, line.strip('\n'))
        m2 = re.match(p_test2, line.strip('\n'))
        if m1:
            iteration.append(int(m1.group('iteration')))
        if m2:
            accuracy.append(float(m2.group('accuracy')))
    drawPlot(iteration, accuracy)

import matplotlib.pyplot as plt
def drawPlot(x, y):
    plt.plot(x, y)
    plt.ylim(0, 1)  # y坐标轴最小值、最大值分别设置为X最小值和最大值的1.1
    plt.yticks(np.linspace(0, 1, 10))  # 显示+-π,+-π/2的刻度
    maxAccuracy = max(y)
    index = y.index(maxAccuracy)
    iteration = x[index]
    plt.ylabel('accuracy')
    plt.xlabel('max accuracy %f iter %d:' % (maxAccuracy, iteration))
    plt.grid()
    plt.show()


def save_classified_photos(result_file, save_path):
    for line in open(result_file):
        line = line.strip('\n')
        temp = line.split(' ')
        if len(temp)==2:
            filepath = temp[0]
            label = temp[1]
            filename = os.path.split(filepath)[1]

            save_path_label = os.path.join(save_path, label)
            save_file_name = os.path.join(save_path_label, filename)
            print filepath, save_file_name
            if not os.path.exists(save_path_label):
                os.makedirs(save_path_label)
            shutil.copy(filepath, os.path.join(save_path_label, save_file_name))


if __name__ == '__main__':
    makefilelist('/home/leo/AvatarDatabase/face6.2/test', False)
    print len(file_list)