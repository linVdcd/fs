//
// Created by leo on 17-8-22.
//

#ifndef FACESHAPEPREDICT_PREDICTFACESHAPE_H
#define FACESHAPEPREDICT_PREDICTFACESHAPE_H
#include <caffe/caffe.hpp>
#ifdef USE_OPENCV
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#endif  // USE_OPENCV
#include <algorithm>
#include <iosfwd>
#include <memory>
#include <string>
#include <utility>
#include <vector>

using namespace caffe;  // NOLINT(build/namespaces)
using std::string;

/* Pair (label, confidence) representing a prediction. */
typedef std::pair<string, float> Prediction;

class Classifier {
public:
    /**
     * 有mean file 文件
     * @param model_file
     * @param trained_file
     * @param mean_file
     * @param label_file
     */
    Classifier(const string& model_file,
               const string& trained_file,
               const string& mean_file,
               const string& label_file);

    /**
     * 没有mean file文件
     * @param model_file
     * @param trained_file
     * @param label_file
     */
    Classifier(const string& model_file,
               const string& trained_file,
               const string& label_file);

    std::vector<Prediction> Classify(const cv::Mat& img, int N = 5);

private:
    void SetMean(const string& mean_file);
    void SetMean();
    std::vector<float> Predict(const cv::Mat& img);

    void WrapInputLayer(std::vector<cv::Mat>* input_channels);

    void Preprocess(const cv::Mat& img,
                    std::vector<cv::Mat>* input_channels);

private:
    shared_ptr<Net<float> > net_;
    cv::Size input_geometry_;
    int num_channels_;
    cv::Mat mean_;
    std::vector<string> labels_;
//    cv::Scalar s_;
};
#endif //FACESHAPEPREDICT_PREDICTFACESHAPE_H
