# -*- coding: utf-8 -*-
import utils
import guis

if __name__ == '__main__':
    opt = guis.draw_main_gui()
    # importcaffe()
    if opt == '1':
        utils.u_makefilelist()
    elif opt == '2':
        utils.u_cropFace()
    elif opt == '3':
        utils.u_make_lmdb()
    elif opt == '4':
        utils.u_run_train()
    elif opt == '5':
        utils.u_parse_log()
    elif opt == '6':
        utils.u_predict()
    elif opt == '7':
        utils.u_get_accuracy()
    elif opt == '8':
        utils.u_classify_photos()
    elif opt == '9':
        utils.u_save_classified_photos()
    else:
        pass