#!/usr/bin/env sh
# Create the caffe net lmdb inputs

OUT=$1  # LMDB存放路径
DATA=$2  # 图片所在路径
filelist=$3

## resize 图片大小
RESIZE_HEIGHT=$4
RESIZE_WIDTH=$5
caffe_root=$6

# caffe的Tools路径
TOOLS=$caffe_root/build/tools

# 如果目录不存在，则新建目录
if [ ! -d $OUT ]; then
  mkdir $OUT
fi
# 先删除已经存在的旧的lmdb
rm -rf $OUT

echo "Creating $OUT ..."
GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $DATA/ \
    $filelist \
    $OUT
echo "Done."
