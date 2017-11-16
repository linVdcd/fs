# -*- coding: utf-8 -*-
from __future__ import division
import sys
import os
import functions
import dlib
from multiprocessing import Pool


def u_importcaffe():
    """
    导入caffe模块
    :return:
    """
    caffe_root = raw_input("> 请输入caffe所在路径(/home/leo/caffe): ") or '/home/leo/caffe'
    sys.path.insert(0, os.path.join(caffe_root, 'python'))
    try:
        import caffe
    except Exception, e:
        # raise Exception("caffe 路径错误！")
        print '您输入的路径有误，请确认路劲是否正确或caffe是否安装成功!'
        u_importcaffe()
    else:
        print '> import caffe module successful!'

def u_makefilelist():
    """
    制作图像文件列表
    :return:
    """
    os.system('clear')
    image_root_path = raw_input('> 请输入图片所在的根目录\n(example:/xxx/xxx/images/class01/0001.jpg\nthe input is like \
    this:/xxx/xxx/images): ')
    while not os.path.exists(image_root_path):
        image_root_path = raw_input('> 您输入的路劲不存在，请重新输入: ')

    save_file_path = raw_input('> 请输入要保存的文件名(默认为当前目录下filelist.txt): ') or './filelist.txt'
    while True:
        front_save_path = os.path.split(save_file_path)[0]
        if front_save_path == '':
            front_save_path = '.'
        if not os.path.exists(front_save_path):
            save_file_path = raw_input('> 您输入的路径不存在，请重新输入: ') or './filelist.txt'
        else:
            if not save_file_path.endswith('.txt'):
                save_file_path += '.txt'
            break
    label = raw_input("> 是否要添加label(y/n)默认为(n): ") or 'n'
    while True:
        if label in ['y', 'Y']:
            label = True
            break
        elif label in ['n', 'N']:
            label = False
            break
        else:
            label = raw_input("> 是否要添加label(y/n)默认为(n): ") or 'n'
    functions.makefilelist(image_root_path, label=label)
    with open(save_file_path, 'w') as fw:
        for image_path in functions.file_list:
            fw.write(image_path)
    print 'make', os.path.abspath(save_file_path), 'successful!'


def u_cropFace():
    """
    裁剪人脸图片
    :return:
    """
    filelist = raw_input("> 请输入图片列表文件: ") or "./filelist.txt"
    while not os.path.exists(filelist):
        filelist = raw_input("> 文件不存在，请重新输入: ") or "./filelist.txt"

    # shape_predictor_68_face_landmarks_path = raw_input("> 请输入 shape_predictor_68_face_landmarks 文件路径,默认为\
    # (./appendix/shape_predictor_68_face_landmarks.dat): ") or "./appendix/shape_predictor_68_face_landmarks.dat"
    # while not os.path.exists(shape_predictor_68_face_landmarks_path):
    #     shape_predictor_68_face_landmarks_path = raw_input("> 文件不存在，请重新输入: ") or "./appendix/shape_predictor_68_face_landmarks.dat"

    no_face_images_dir = raw_input("> 请输入检测不到人脸的图片存放路径,默认为(./no_face_images): ") or './no_face_images'  # 检测不到人脸的图片存放目录
    while os.path.exists(no_face_images_dir):
        query = raw_input("> 该目录已经存在，将删除该目录下的所有文件，是否删除?(y|n)n: ") or 'n'
        if query in ['y', 'Y']:
            os.system('rm -rf ' + no_face_images_dir)
        else:
            no_face_images_dir = raw_input("> 请重新选择路径: ") or './no_face_images'  # 检测不到人脸的图片存放目录
    os.makedirs(no_face_images_dir)

    multiface_images_dir = raw_input("> 请输入检测到多张人脸的图片存放路径，默认为(./multiface_images): ") or './multiface_images'  # 检测到多张人脸的图片存放目录
    while os.path.exists(multiface_images_dir):
        query = raw_input("> 该目录已经存在，将删除该目录下的所有文件，是否删除?(y|n)n: ") or 'n'
        if query in ['y', 'Y']:
            os.system('rm -rf ' + multiface_images_dir)
        else:
            multiface_images_dir = raw_input("> 请重新选择路径: ") or './multiface_images'
    os.makedirs(multiface_images_dir)

    # predictor = dlib.shape_predictor(shape_predictor_68_face_landmarks_path)  # 特征点预测
    detector = dlib.get_frontal_face_detector()  # 人脸检测
    save_path = raw_input("> 请输入裁剪过的人脸图片存放路劲,默认为(./crop): ") or './crop'
    while os.path.exists(save_path):
        query = raw_input("> 该目录已经存在，将删除该目录下的所有文件，是否删除?(y|n)n: ") or 'n'
        if query in ['y', 'Y']:
            os.system('rm -rf ' + save_path)
        else:
            save_path = raw_input("> 请重新选择路径 ") or './crop'
    os.makedirs(save_path)

    # rescale = [1.185974, 0.4, 1.135600, 1.3]  # 裁剪参数
    rescale = raw_input("> 请输入裁剪参数,默认为[1.2 0.30 1.2 1.5]: ") or '1.2 0.30 1.2 1.5'
    while True:
        try:
            rescale = [float(x) for x in rescale.split(' ')]
            break
        except:
            rescale = raw_input("> 您输入的参数有误,请重新输入，默认为[1.2 0.30 1.2 1.5]: ") or '1.2 0.30 1.2 1.5'

    # for line in open(filelist):
    #     functions.cropFace(line,detector, save_path, rescale, no_face_images_dir, multiface_images_dir)

    pool = Pool(processes=5)  # set the processes max number 3
    for line in open(filelist, 'r'):
        pool.apply_async(functions.cropFace, (line.strip('\n'), detector, save_path, rescale, no_face_images_dir, multiface_images_dir))
    pool.close()
    pool.join()
    print "sub-process(es) done."


def u_make_lmdb():
    caffe_root = raw_input("> 请输入caffe所在路径,默认为(/home/leo/caffe): ") or '/home/leo/caffe'
    while not os.path.exists(caffe_root):
        caffe_root = raw_input("> 您输入的路径不存在,请重新输入(/home/leo/caffe): ") or '/home/leo/caffe'

    image_path = raw_input("> 请输入图片所在根目录的绝对路径(/home/leo/xx/xx/images): ") or './not_exist'
    image_path = os.path.abspath(image_path)
    while not os.path.exists(image_path):
        image_path = raw_input("> 您输入的路径不存在,请重新输入: ") or './not_exist'

    filelist_with_label = raw_input("> 请输入带标签的图片列表文件(filelist.txt): ") or './not_exist'
    while not os.path.exists(filelist_with_label):
        image_path = raw_input("> 您输入的文件不存在,请重新输入: ") or './not_exist'

    lmdb_path = raw_input("> 请输入lmdb路径,example(./lmdb/train_lmdb): ") or './lmdb/train_lmdb'
    if not os.path.exists(os.path.split(lmdb_path)[0]):
        os.makedirs(os.path.split(lmdb_path)[0])
    resize_height = raw_input("> 请输入resize height大小,默认为256: ") or '256'
    resize_width = raw_input("> 请输入resize weight大小,默认为256: ") or '256'
    cmd = "sh shscripts/create_lmdb.sh %s %s %s %s %s %s" % (lmdb_path, os.path.split(image_path)[0], filelist_with_label, \
                                                             resize_height, resize_width, caffe_root)
    print cmd
    os.system(cmd)


def u_run_train():
    caffe_root = raw_input("> 请输入caffe所在路径,默认为(/home/leo/caffe): ") or '/home/leo/caffe'
    while not os.path.exists(caffe_root):
        caffe_root = raw_input("> 您输入的路径不存在,请重新输入(/home/leo/caffe): ") or '/home/leo/caffe'

    solver_file = raw_input("> 请输入solver文件,默认为(./solver.prototxt): ") or './solver.prototxt'
    while not os.path.exists(solver_file):
        solver_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './solver.prototxt'

    weights_file = raw_input("> 请输入用于finetune的weights文件,默认为(./weights_file.caffemodel): ") or './weights_file.caffemodel'
    while not os.path.exists(weights_file):
        weights_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './weights_file.caffemodel'

    gpu_index = raw_input("> 请输入使用的GUP号,默认为0: ") or '0'

    log = raw_input("> 请输入日志文件的文件名,默认为(./log.txt): ") or './log.txt'
    while not os.path.exists(os.path.split(log)[0]):
        log = raw_input("> 您输入的文件的父路径不存在,请重新输入: ") or './log.txt'

    cmd = "run ./shscripts/run_train.sh %s %s %s %s" % (caffe_root, solver_file, weights_file, gpu_index, log)
    os.system(cmd)


def u_predict():
    deploy_file = raw_input("> 请输入deploy.prototxt路径: ") or './appendix/net.prototxt'
    while not os.path.exists(deploy_file):
        deploy_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './appendix/net.prototxt'

    model_file = raw_input("> 请输入model.modelcaffe路径: ") or './appendix/model.caffemodel'
    while not os.path.exists(model_file):
        model_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './appendix/model.caffemodel'

    image_path = raw_input("> 请输入图片路径路径: ") or './test.jpg'
    while not os.path.exists(image_path):
        image_path = raw_input("> 您输入的路径不存在,请重新输入: ") or './test.jpg'

    order = functions.predict(image_path, deploy_file, model_file)
    print order


def u_get_accuracy():
    deploy_file = raw_input("> 请输入deploy.prototxt路径: ") or './appendix/net.prototxt'
    while not os.path.exists(deploy_file):
        deploy_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './appendix/net.prototxt'

    model_file = raw_input("> 请输入model.modelcaffe路径: ") or './appendix/model.caffemodel'
    while not os.path.exists(model_file):
        model_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './appendix/model.caffemodel'

    filelist = raw_input("> 请输入图片列表文件(testlist_with_label.txt): ") or './testlist.txt'
    while not os.path.exists(filelist):
        filelist = raw_input("> 您输入的路径不存在,请重新输入: ") or './testlist.txt'

    print functions.get_accuracy(filelist, deploy_file, model_file)


def u_classify_photos():
    deploy_file = raw_input("> 请输入deploy.prototxt路径: ") or './appendix/net.prototxt'
    while not os.path.exists(deploy_file):
        deploy_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './appendix/net.prototxt'

    model_file = raw_input("> 请输入model.modelcaffe路径: ") or './appendix/model.caffemodel'
    while not os.path.exists(model_file):
        model_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './appendix/model.caffemodel'

    filelist = raw_input("> 请输入要分类图片列表文件路径: ") or './photos_list.txt'
    while not os.path.exists(filelist):
        filelist = raw_input("> 您输入的路径不存在,请重新输入: ") or './photos_list.txt'

    result_file = raw_input("> 请输入分类结果保存文件名(classify_result.txt): ") or './classify_result.txt'
    while os.path.exists(result_file):
        result_file = raw_input("> 您输入的路径已存在,请重新输入: ") or './classify_result.txt'

    functions.classify_photos(filelist, deploy_file, model_file)
    with open(result_file, 'w') as fw:
        for line in functions.global_list:
            fw.write(line)


def u_save_classified_photos():
    result_file = raw_input("> 请输入保存分类结果的文件名(classify_result.txt): ") or './classify_result.txt'
    while not os.path.exists(result_file):
        result_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './classify_result.txt'
    save_path = raw_input("> 请输要保存的的路径(./class_result): ") or './class_result'
    while not os.path.exists(save_path):
        save_path = raw_input("> 您输入的路径不存在,请重新输入: ") or './class_result'
    functions.save_classified_photos(result_file, save_path)


def u_parse_log():
    log_file = raw_input("> 请输入log.txt路径: ") or './log.txt'
    while not os.path.exists(log_file):
        log_file = raw_input("> 您输入的路径不存在,请重新输入: ") or './log.txt'

    functions.parse_log(log_file)