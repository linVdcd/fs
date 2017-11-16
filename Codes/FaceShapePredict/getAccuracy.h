//
// Created by leo on 17-8-23.
//

#ifndef FACESHAPEPREDICT_GETACCURACY_H
#define FACESHAPEPREDICT_GETACCURACY_H

#include "predictFaceShape.h"
#include "getStandardFace.h"
#include <cassert>
std::string getSingleImageFaceshape(std::string file_name, Classifier &classifier, dlib::frontal_face_detector &detector, dlib::shape_predictor &sp, float rescale[]);
void getMultiImageFaceshape(std::string file_list, std::string results_file, Classifier &classifier, dlib::frontal_face_detector &detector, dlib::shape_predictor &sp, float rescale[]);
#endif //FACESHAPEPREDICT_GETACCURACY_H
