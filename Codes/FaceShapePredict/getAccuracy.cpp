//
// Created by leo on 17-8-23.
//

#include "getAccuracy.h"

std::string getSingleImageFaceshape(std::string file_name, Classifier &classifier, dlib::frontal_face_detector &detector, dlib::shape_predictor &sp, float rescale[]) {
    cv::Rect rect = getFaceBox(file_name, detector, sp);
    cv::Mat img = getFaceImage(file_name, rect, rescale);

    CHECK(!img.empty()) << "Unable to decode image " << file_name;
    std::vector<Prediction> predictions = classifier.Classify(img);

    /* Print the top N predictions. */
//    for (size_t i = 0; i < predictions.size(); ++i) {
//        Prediction p = predictions[i];
//        std::cout << std::fixed << std::setprecision(4) << p.second << " - \""
//                  << p.first << "\"" << std::endl;
//    }
//    cv::imwrite("test_crop.jpg", face);  // 将裁剪过后的图片保存
//    cv::imshow("face", img);  // 显示图片
//    cv::waitKey(0);
    return  predictions[0].first;
}

void getMultiImageFaceshape(std::string file_list, std::string results_file, Classifier &classifier, dlib::frontal_face_detector &detector, dlib::shape_predictor &sp, float rescale[]) {
    std::ifstream infile;  // 读文件流
    std::ofstream outfile;  // 写文件流
    infile.open(file_list);  // 打开图片列表文件
    outfile.open(results_file);  // 打开保存结果文件

//    assert(infile.is_open());  // 如果打开失败，则中断
//    assert(outfile.is_open());
    if(infile.is_open() == false){
        std::cout << "打开" << file_list << "文件失败" << std::endl;
        return;
    }

    if(outfile.is_open() == false){
        std::cout << "打开" << results_file << "文件失败" << std::endl;
        return;
    }
    std::string file_name;  // 要预测的图片文件名
    while(getline(infile, file_name)) {
        std::cout << "---------- Prediction for "
                  << file_name << " ----------" << std::endl;

        cv::Rect rect = getFaceBox(file_name, detector, sp);
        cv::Mat img = getFaceImage(file_name, rect, rescale);

        CHECK(!img.empty()) << "Unable to decode image " << file_name;
        std::vector<Prediction> predictions = classifier.Classify(img);

        outfile << file_name << "\n";
        /* Print the top N predictions. */
        for (size_t i = 0; i < predictions.size(); ++i) {
            Prediction p = predictions[i];
            std::cout << std::fixed << std::setprecision(4) << p.second << " - \""
                      << p.first << "\"" << std::endl;
            // 将预测结果写入文件
            outfile << std::fixed << std::setprecision(4) << p.second << " - \""
                    << p.first << "\"\n";
        }
        outfile.flush();
        //cv::imwrite("test_crop.jpg", img);  // 将裁剪过后的图片保存
        cv::imshow("face", img);  // 显示图片
        cv::waitKey(0);
    }
    // 关闭文件流
    infile.close();
    outfile.flush();
    outfile.close();
}