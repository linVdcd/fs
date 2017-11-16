#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=../LMDB/faceshape6.1_lmdb/
DATA=../LMDB/faceshape6.1_lmdb/
TOOLS=/home/leo/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/train6.1_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."
