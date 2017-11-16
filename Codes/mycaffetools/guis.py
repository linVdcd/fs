# -*- coding: utf-8 -*-
def draw_main_gui():
    """
    绘制初始字符界面
    :return:
    """
    tb = '='
    lr = '|'
    message = 'WELCOME TO USE MY CAFFE TOOLS!'
    opt1 = '1. make file list'
    opt2 = '2. crop face'
    opt3 = '3. make lmdb'
    opt4 = '4. run train'
    opt5 = '5. watch train log'
    opt6 = '6. predit a single image'
    opt7 = '7. test accuracy'
    opt8 = '8. classify photos by file list'
    opt9 = '9. save photos by classify txt '
    opt0 = '0. quit'

    l = len(message)
    span = 5
    top_bottom = tb * (l + 2 * span + 2)
    left_right = lr+' '*(l+2*span)+lr
    print top_bottom
    print left_right
    print lr+' '*span+message+' '*span+lr
    print lr + ' ' * span + opt1 + ' ' * (span + (l - len(opt1))) + lr
    print lr + ' ' * span + opt2 + ' ' * (span + (l - len(opt2))) + lr
    print lr + ' ' * span + opt3 + ' ' * (span + (l - len(opt3))) + lr
    print lr + ' ' * span + opt4 + ' ' * (span + (l - len(opt4))) + lr
    print lr + ' ' * span + opt5 + ' ' * (span + (l - len(opt5))) + lr
    print lr + ' ' * span + opt6 + ' ' * (span + (l - len(opt6))) + lr
    print lr + ' ' * span + opt7 + ' ' * (span + (l - len(opt7))) + lr
    print lr + ' ' * span + opt8 + ' ' * (span + (l - len(opt8))) + lr
    print lr + ' ' * span + opt9 + ' ' * (span + (l - len(opt9))) + lr
    print lr + ' ' * span + opt0 + ' ' * (span + (l - len(opt0))) + lr
    print left_right
    print top_bottom
    opt = raw_input('> 请选择您的操作: ') or 'n'
    while True:
        if opt in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return opt
        else:
            opt = raw_input('> 请选择0-8的选项: ') or 'n'