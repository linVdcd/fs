//
// Created by leo on 17-8-21.
//

#ifndef FACESHAPEAPI_GETSTANDARDFACE_H
#define FACESHAPEAPI_GETSTANDARDFACE_H

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <dlib/image_processing/frontal_face_detector.h>
#include <dlib/image_processing/render_face_detections.h>
#include <dlib/image_processing.h>
#include <dlib/image_io.h>
cv::Rect getFaceBox(std::string image_path, dlib::frontal_face_detector &detector, dlib::shape_predictor &predictor);
cv::Mat getFaceImage(std::string image_path, cv::Rect rect, float rescal[]);
#endif //FACESHAPEAPI_GETSTANDARDFACE_H
