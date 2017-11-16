#!/usr/bin/env sh
# Create the caffe net lmdb inputs
CAFFE_ROOT=$1
FILE_LIST=$2
IMAGES_PATH=$3
LMDB_PATH=$4
LMDB_NAME=$5
RESIZE_HEIGHT=$6
RESIZE_WIDTH=$7

# caffe的Tools路径
TOOLS=$CAFFE_ROOT/build/tools

# 如果目录不存在，则新建目录
if [ ! -d $LMDB_PATH ]; then
  mkdir $LMDB_PATH
fi

# 先删除已经存在的旧的lmdb
rm -rf $LMDB_PATH/$LMDB_NAME

echo "Creating $LMDB_PATH/$LMDB_NAME ..."
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $IMAGES_PATH/ \
    $FILE_LIST \
    $LMDB_PATH/$LMDB_NAME
echo "Done."
