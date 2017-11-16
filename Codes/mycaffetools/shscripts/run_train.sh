#!/usr/bin/env sh
caffe_root = $1
solver = $2
weights = $3
gpu = $4
log = $5
TOOLS=$caffe_root/build/tools
$TOOLS/caffe train -solver $solver -weights $weights -gpu $gpu 2>&1 | tee $log
