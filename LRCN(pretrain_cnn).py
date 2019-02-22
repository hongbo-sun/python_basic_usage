#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:44:50 2018

@author: hongbo_sun

pretrained CNN
"""
import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, Flatten, Dropout, Reshape, Permute, Activation,Input,Average
from keras.layers import Convolution2D, MaxPooling3D, ConvLSTM2D,Conv3D
from keras.layers.recurrent import LSTM
import keras.callbacks
import os, random




from sklearn import preprocessing
from keras.models import Sequential
from keras.preprocessing import image
from keras.models import Model
from keras.applications.inception_v3 import InceptionV3
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.resnet50 import ResNet50
#from keras.applications.vgg16 import preprocess_input
#from keras.applications.resnet50 import preprocess_input
#from keras.applications.inception_v3 import preprocess_input
from keras.layers.core import Dropout
import numpy as np
from keras.utils import np_utils, generic_utils
from keras.optimizers import SGD
from keras.layers import Dense, GlobalAveragePooling2D,Convolution2D,Activation,MaxPooling2D,Flatten,GlobalMaxPooling2D,Reshape
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import optimizers
import keras
import time
from keras import metrics
from keras.callbacks import ModelCheckpoint
import os
from PIL import Image
import tensorflow as tf
import keras.backend.tensorflow_backend as KTF
#from keras.applications.imagenet_utils import preprocess_input
from keras.models import load_model
import matplotlib.pyplot as plt
from keras.layers import TimeDistributed



import sys




sys.setrecursionlimit(1000000000)












if __name__ == '__main__':
    base_model=VGG16(include_top=False,weights= 'imagenet',input_shape=(224,224,3))

    
    vmodel=base_model.get_layer(index=17).output
    vmodel=Dense(4096, activation='relu')(vmodel)
    vmodel=Dropout(0.5, noise_shape=(1,))(vmodel)
    vmodel=Dense(1024, activation='relu')(vmodel)
    #vmodel=Dropout(0.5)(vmodel)
    vmodel=Flatten()(vmodel)
    vmo=Dense(101, activation='softmax')(vmodel)                           
    model_ = Model(inputs=base_model.input, outputs=vmo)
    print(model_.summary())
    
    
    
    input_sequences=Input(shape=(30, 224,224,3))
    processed_sequences = TimeDistributed(model_)(input_sequences)
    output=keras.layers.pooling.GlobalAveragePooling1D()(processed_sequences)
    model = Model(inputs=input_sequences, outputs=output)
    print(model.summary())
   
    
    
    

