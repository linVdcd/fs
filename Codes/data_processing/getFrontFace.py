# -*- coding: utf-8 -*-

import dlib
from skimage import io
import Image
import multiprocessing as mp
import numpy as np
import matplotlib.pyplot as plt
import os
import random

predictor_path = "utils/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def getFaceBoundingBox(image_path, save_path, crop_params):
    print image_path
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 随机裁剪参数

    img = io.imread(image_path)
    im = Image.open(image_path)
    dets = detector(img, 1)
    if len(dets) != 1:
        print "检测不到人脸，或有多张人脸，跳过",image_path
        # return
    else:
        shape = predictor(img, dets[0])
        xs = []  # landmark点x坐标列表
        ys = []  # landmark点y坐标列表
        for i in range(68):
            point = shape.part(i)
            xs.append(point.x)
            ys.append(point.y)
        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)

        min_x_real = min_x - int((max_x - min_x)*crop_params[0])
        max_x_real = max_x + int((max_x - min_x) * crop_params[2])
        min_y_real = min_y + int((max_y-min_y)*crop_params[1])
        max_y_real = max_y + int((max_y-min_y)*crop_params[3])
        if min_x_real < 0:
            min_x_real = 0
        if max_x_real > img.shape[0]:
            max_x_real = img.shape[0]
        if max_y > img.shape[1]:  # 如果裁剪高度超出图片高度
            max_y_real = img.shape[1]
        width = max_x_real - min_x_real
        height = max_y_real - min_y_real
        if width > height:
            height = width
        else:
            width = height
        box = (min_x_real, min_y_real, max_x_real, max_y_real)
        face = im.crop(box)
        squre_face = Image.new('RGB', (width, height), (0, 0, 0))
        # print squre_face.mode, squre_face.size
        squre_face.paste(face, (int((width-face.size[0])/2), int((height-face.size[1])/2)))
        image_name = str(i)+"_"+os.path.split(image_path)[1]
        squre_face.save(os.path.join(save_path, image_name))
        # det = dlib.rectangle(min_x, min_y, max_x, max_y)  # 构造boundingbox
        # win = dlib.image_window()
        # win.clear_overlay()
        # win.set_image(squre_face)
        # win.add_overlay(det)
        # dlib.hit_enter_to_continue()


def getRandomFaceBoundingBox(image_path, save_path, params):
    print image_path
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 随机裁剪参数

    img = io.imread(image_path)
    im = Image.open(image_path)
    dets = detector(img, 1)
    if len(dets) != 1:
        print "检测不到人脸，或有多张人脸，跳过",image_path
        # return
    else:
        shape = predictor(img, dets[0])
        xs = []  # landmark点x坐标列表
        ys = []  # landmark点y坐标列表
        for i in range(68):
            point = shape.part(i)
            xs.append(point.x)
            ys.append(point.y)
        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)

        for i in range(5):
            crop_params = [random.uniform(params[0]-0.02, params[0]+0.03), random.uniform(params[1]-0.02, params[1]+0.03),
                           random.uniform(params[2]-0.02, params[2]+0.03),random.uniform(params[3]-0.02, params[3]+0.03)]
            min_x_real = min_x - int((max_x - min_x)*crop_params[0])
            max_x_real = max_x + int((max_x - min_x) * crop_params[2])
            min_y_real = min_y + int((max_y-min_y)*crop_params[1])
            max_y_real = max_y + int((max_y-min_y)*crop_params[3])
            if min_x_real < 0:
                min_x_real = 0
            if max_x_real > img.shape[0]:
                max_x_real = img.shape[0]
            if max_y > img.shape[1]:  # 如果裁剪高度超出图片高度
                max_y_real = img.shape[1]
            width = max_x_real - min_x_real
            height = max_y_real - min_y_real
            if width > height:
                height = width
            else:
                width = height
            box = (min_x_real, min_y_real, max_x_real, max_y_real)
            face = im.crop(box)
            squre_face = Image.new('RGB', (width, height), (0, 0, 0))
            # print squre_face.mode, squre_face.size
            squre_face.paste(face, (int((width-face.size[0])/2), int((height-face.size[1])/2)))
            name_etx = os.path.split(image_path)[1].split(".")
            image_name = name_etx[0]+"_"+str(i)+"."+name_etx[1]
            squre_face.save(os.path.join(save_path, image_name))
            # det = dlib.rectangle(min_x, min_y, max_x, max_y)  # 构造boundingbox
            # win = dlib.image_window()
            # win.clear_overlay()
            # win.set_image(squre_face)
            # win.add_overlay(det)
            # dlib.hit_enter_to_continue()


def cropFace(file_list, save_path, crop_params):
    images = [file.strip('\n') for file in open(file_list).readlines()]
    pool = mp.Pool()
    [pool.apply_async(getFaceBoundingBox, args=(image_path.strip('\n'), os.path.join(save_path, image_path.split('/')[-2]), crop_params)) for image_path in images]
    pool.close()
    pool.join()

def cropRandomFace(file_list, save_path, crop_params):
    images = [file.strip('\n') for file in open(file_list).readlines()]
    pool = mp.Pool()
    [pool.apply_async(getRandomFaceBoundingBox, args=(image_path.strip('\n'), os.path.join(save_path, image_path.split('/')[-2]), crop_params)) for image_path in images]
    pool.close()
    pool.join()


if __name__ == "__main__":
    # val_file_list = "/home/leo/AvatarData/face8.0/val.txt"
    # val_save_path = "/home/leo/AvatarData/face8.0/val_crop"
    # train_file_list = "/home/leo/AvatarData/face8.0/train.txt"
    # train_save_path = "/home/leo/AvatarData/face8.0/train_crop"
    # cropFace(val_file_list, val_save_path)
    # cropFace(train_file_list, train_save_path, crop_params)
    # getFaceBoundingBox("images/001.jpg", "crops")
    filelist = "test/val.txt"
    save_path = "test"
    cropFace(filelist, save_path)
    print 'end'
