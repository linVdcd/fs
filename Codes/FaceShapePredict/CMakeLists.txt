cmake_minimum_required(VERSION 2.8.8)
project(FaceShapePredict)

set(CMAKE_CXX_STANDARD 11)
set(Caffe_DIR /home/leo/caffe/build)
find_package(Caffe REQUIRED)
if (NOT Caffe_FOUND)
    message(FATAL_ERROR "Caffe NOT Fund!")
endif (NOT Caffe_FOUND)

include_directories(${Caffe_INCLUDE_DIRS})
INCLUDE(/home/leo/dlib-19.4/dlib/cmake)
add_definitions(${Caffe_DEFINITIONS}) # ex. -DCPU_ONLY

set(SOURCE_FILES main.cpp getStandardFace.h getStandardFace.cpp predictFaceShape.h predictFaceShape.cpp getAccuracy.h getAccuracy.cpp)
add_executable(FaceShapePredict ${SOURCE_FILES})

target_link_libraries(FaceShapePredict ${Caffe_LIBRARIES} dlib)