import sys
import numpy as np
caffe_root = '/home/leo/caffe'
sys.path.insert(0, caffe_root+'python')
import caffe

class Predict:
    def __init__(self, deployfile, modelfile, softmax_layer_name='prob', scale=255, meanfile=None):
        self.deployfile = deployfile
        self.modelfile = modelfile
        self.softmax_layer_name = softmax_layer_name
        self.scale = scale
        self.meanfile = meanfile

    def load_model(self):
        return caffe.Net(self.deployfile, self.modelfile, caffe.TEST)

    def get_transformer(self, net):
        transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
        transformer.set_transpose('data', (2, 0, 1))
        if self.meanfile:
            transformer.set_mean('data', np.load(self.meanfile).mean(1).mean(1))
        transformer.set_raw_scale('data', self.scale)
        transformer.set_channel_swap('data', (2, 1, 0))
        return transformer

    def predict(self, image_path, net, transformer):
        img = caffe.io.load_image(image_path)
        net.blobs['data'].data[...] = transformer.preprocess('data', img)
        out = net.forward()
        prob = net.blobs[self.softmax_layer_name].data[0].flatten()
        order = prob.argsort()[-1]
        return order
