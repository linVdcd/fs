//
// Created by leo on 17-8-21.
//
#include "getStandardFace.h"
cv::Rect getFaceBox(std::string image_path, dlib::frontal_face_detector &detector, dlib::shape_predictor &sp) {
    cv::Rect rect(0, 0, 0, 0);
    try {
//        std::cout << "> processing image " << image_path << std::endl;
        dlib::array2d<dlib::rgb_pixel> img;
        dlib::load_image(img, image_path);

        // 现在，告诉人脸检测器，给出所有人脸周围的bounding box列表
        std::vector<dlib::rectangle> dets = detector(img);
//        std::cout<< "> 检测到 " << dets.size() << "张人脸" << std::endl;
        // 如果一张图片中有多张人脸，则跳过该张图片
//        assert(dets.size()==1);
        // 这里只取第一张人脸
        dlib::rectangle det = dets[0];
        // 现在我们使用shape_predictor来告诉我们检测到的人脸的姿态
        dlib::full_object_detection shape = sp(img, det);

        // 获取bounding box

        long left=det.left(), top=det.top(), right=det.right(), bottom=det.bottom();
        for(int i=0; i<68; i++) {
            long x = shape.part(i).x();
            long y = shape.part(i).y();
            if(x<left)
                left = x;
            if(y<top)
                top = y;
            if(x>right)
                right = x;
            if(y>bottom)
                bottom=y;
        }
        rect.x = left;
        rect.y = top;
        rect.width = right -left;
        rect.height = bottom - top;

//        dlib::image_window win_face;  // 显示图片窗口
//        // 在图片上显示bounding box
//        win_face.clear_overlay();
//        win_face.set_image(img);
//        win_face.add_overlay(box, dlib::rgb_pixel(255, 0, 0));
//
//
//        std::vector<dlib::full_object_detection> shapes;
//        shapes.push_back(shape);
//        // 在图片上显示landmark
//        win_face.set_image(img);
//        win_face.add_overlay(dlib::render_face_detections(shapes));
//
//        std::cout << "按Enter键结束..." << std::endl;
//        std::cin.get();
    } catch (std::exception &e) {
        std::cout << "\n抛出异常!" << std::endl;
        std::cout << e.what() << std::endl;
    }
    return rect;
}

cv::Mat getFaceImage(std::string image_path,cv::Rect rect, float rescale[]) {
    cv::Mat src = cv::imread(image_path);
//    std::cout << "> 图片大小: " << src.size << std::endl;
    float l = rescale[0]; // 往左扩展系数
    float t = rescale[1]; // 往下偏移系数
    float r = rescale[2]; // 往右扩展系数
    float b = rescale[3]; // 往下扩展系数
    long width = rect.width, height = rect.height;
    long left = rect.x + int(width*l);
    long top = rect.y + int(height*t);
    long right = rect.x + int(width*(1+r));
    long bottom = rect.y + int(height*(1+b));
    // 确保裁剪框不超出图片范围
    if(left<0)
        left = 0;
    if(right>src.size[0])
        right = src.size[0];
    if(bottom>src.size[1])
        bottom = src.size[1];

    // 需要将图片padding成正方形
    long new_width = right - left;
    long new_height = bottom - top;
    long edge_len = new_height;
    if(edge_len < new_width)
        edge_len = new_width;

//    // 选取指定区域图片，方法1
//    cv::Rect new_rect(left, top, edge_len, edge_len);
//    cv::Mat temp(src, new_rect);

    // 选取指定区域图片，方法2
    cv::Mat temp = src.colRange(left, right).rowRange(top, bottom);
//    std::cout << "> 正方形大小: " << temp.size << std::endl;
    cv::Mat dst = cv::Mat::zeros(edge_len,edge_len, CV_8UC3);
    // 为了使图片显示在正方形中间位置，计算上边距和左边距
    long left_padding = (edge_len-new_width)/2;
    long top_padding = (edge_len-new_height)/2;
//    std::cout << "left_padding:" << left_padding << ", top_padding:" << top_padding << std::endl;
//    std::cout << "edge_len:" << edge_len << ", (top, bottom),(left, right): (" << top_padding << "," << edge_len-top_padding << "),(" << left_padding << "," << edge_len-left_padding << ")" << std::endl;
    // 裁剪
    temp.copyTo(dst.rowRange(top_padding, top_padding+bottom-top).colRange(left_padding, left_padding+right-left));
    return dst;
}