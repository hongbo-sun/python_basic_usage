# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from keras.models import Sequential
from keras.models import load_model
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
from six.moves import range
import random,cPickle
from keras.callbacks import EarlyStopping
import numpy as np
from keras import metrics


import os
from PIL import Image
import numpy as np

import os
from PIL import Image
import numpy as np

import theano
import sys

#from picturesize import picturesize
'''#验证图片的数组存放方式为   (row column channel)以及theano后端时的数据调整方法
sys.setrecursionlimit(1000000000)#系统的递归限制数

picture_num=1
picturefolder="C:\Users\hongb\Desktop\k"
data = np.empty((picture_num,3,224,100),dtype="float32")
label = np.empty((picture_num,),dtype="uint8")
imgs = os.listdir(picturefolder)
num = len(imgs)
for i in range(num):
    img = Image.open(picturefolder+"/"+imgs[i])
    imgg = img.resize((100,224))
    imgg.show()
    arr = np.asarray(imgg,dtype="float32")
    #data[i,:,:,:] = arr[:,:,:]
    data[i,1,:,:] = arr[:,:,1]
    #data[i,2,:,:] = arr[:,:,2]
#print(data)
print(data[:,1,:,:] )
'''

