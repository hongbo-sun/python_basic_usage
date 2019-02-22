# -*- coding: utf-8 -*-
"""
Created on Sat Sep 09 13:19:12 2017

@author: hongb
"""
#函数式模型
from keras.layers import Conv2D,MaxPooling2D,Input,Dense,Activation
from keras.models import Model


img_input = Input(shape=(3,32,32),name='input_0')
x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv1')(img_input)
x = Conv2D(64, (3, 3), activation='relu', padding='same', name='block1_conv2')(x)
x = MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool')(x)
model = Model(img_input, x, name='v')
for i, layer in enumerate(model.layers):
   print(i, layer.name)
print("hello world")






'''#序贯式网络
from __future__ import absolute_import
from __future__ import print_function
from keras.models import Sequential
from keras.models import load_model
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils, generic_utils
from six.moves import range
import random
from keras.callbacks import EarlyStopping
import numpy as np
from keras import metrics
from keras.layers import Conv2D

import os
from PIL import Image
import numpy as np

import os
from PIL import Image
import numpy as np


def create_model():
    # type: () -> object
	model = Sequential()
	model.add(Convolution2D(8, 5, 5, border_mode='valid',input_shape=(1,22,22)))
	model.add(Activation('relu'))





	model.add(Convolution2D(8, 3, 3, border_mode='valid'))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Convolution2D(16,3, 3, border_mode='valid'))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))

	model.add(Flatten())
	model.add(Dense(128, init='normal'))
	model.add(Activation('relu'))

	model.add(Dense(2, init='normal'))
	model.add(Activation('softmax'))
	return model
model1= create_model()
for i, layer in enumerate(model1.layers):
   print(i, layer.name)
'''