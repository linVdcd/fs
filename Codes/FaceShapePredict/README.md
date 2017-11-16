### 1. 依赖
	程序接口依赖，caffe、dlib，使用cmake进行编译，在CMakeList.txt需要添加自己的caffe和dlib的路径。

### 2. 程序入口--main.cpp 需要提供：
	1. model_file	: ./model/deploy.prototxt
	2. trained_model: ./model/mn.caffemodel
	3. label_txt	: ./model/label.txt
	4. dlib_detector: ./utils/shape_predictor_68_face_landmarks.dat

### 3. 程序说明:
	1. 由于训练模型时没有进行减均值操作，所以预测时也不需要减去均值，这里提供Classifier类的重载构造
	函数,根据实际需要，在main函数中选择合适的构造函数：
		需要均值文件：
		Classifier(const string& model_file,
		               const string& trained_file,
		               const string& mean_file,
		               const string& label_file)
		不需要均值文件：
		Classifier(const string& model_file,
		               const string& trained_file,
		               const string& label_file)
	2. getStandardFace.h
	由于在训练网络前，先对图片中的人脸进行裁剪，所以在预测区需要对预测图片进行同样的操作在main函数中，裁剪参数rescale[4] = {-0.05, 0.35, 0.05, 0.08};是比较合适的裁剪参数，其含义是，对dlib检测到的人脸的bounding box 进行 left, top, right, bottom的扩展，该参数将裁剪眼睛以下部分的人脸。

	3. getAccuracy.h
	函数:getSingleImageFaceshape是对单张图片进行脸型预测
	函数:getMultiImageFaceshape是对测试集的所有图片进行预测，需要理工包含label的图片列表文件(注意，需要与label.txt中的顺序相对应)

### 4. 运行程序：
	1. $ cd FaceShapePredict
	2. $ mkdir build
	3. $ cd build
	4. $ cmake ..
	5. $ make all
	6. $ ./FaceShapePredict



