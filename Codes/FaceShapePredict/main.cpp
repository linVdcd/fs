#include <iostream>
#include <fstream>
#include "getAccuracy.h"
int main(int argc, char** argv) {
    ::google::InitGoogleLogging(argv[0]);

//    std::string model_file   = argv[1];
//    std::string trained_file = argv[2];
//    std::string mean_file    = argv[3];
//    std::string label_file   = argv[4];

    std::string model_file   = "../model/net.prototxt";
    std::string trained_file = "../model/mn.caffemodel";
//    std::string mean_file    = "";
    std::string label_file   = "../model/label.txt";


    Classifier classifier(model_file, trained_file, label_file);

    std::string file_list_txt = "../utils/val.txt";  // 测试图片列表文件
    std::string results_txt = "../result2.txt"; // 保存测试结果文件

    // 人脸检测器
    std::string detector_path = "../utils/shape_predictor_68_face_landmarks.dat";
    dlib::frontal_face_detector detector = dlib::get_frontal_face_detector();
    dlib::shape_predictor sp;
    dlib::deserialize(detector_path) >> sp;

    // bounding box {左, 上, 右, 下}扩展系数
    float rescale[4] = {-0.05, 0.35, 0.05, 0.08};  // 调整bounding box参数

    // 测试单个图片文件，输出预测结果
//    std::string filename = "/home/leo/AvatarData/valdata/val/1/00155652.jpg"; // /home/leo/AvatarData/valdata/val/1/00151187.jpg
//    std::cout << "> 预测结果: " << getSingleImageFaceshape(filename, classifier, detector, sp, rescale) << std::endl;

    // 测试所有测试集图片
    getMultiImageFaceshape(file_list_txt, results_txt, classifier, detector, sp, rescale);
    return 0;
}
