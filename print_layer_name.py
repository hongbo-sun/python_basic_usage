# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 19:44:19 2017

@author: hongb
"""

import os
from PIL import Image
import numpy as np


import sys
from keras.models import Sequential
from keras.preprocessing import image
from keras.models import Model
from keras.applications.inception_v3 import InceptionV3
from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications.resnet50 import ResNet50
from keras.applications.vgg16 import preprocess_input
from keras.applications.resnet50 import preprocess_input
from keras.applications.inception_v3 import preprocess_input
from keras.layers.core import Dropout
import numpy as np
from keras.optimizers import SGD
from keras.layers import Dense, GlobalAveragePooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from keras import optimizers
import keras
import time




base_model =VGG16(include_top=True,weights= 'imagenet') 

'''
base_model =VGG16(include_top=False,weights= 'imagenet') 
vmodel=base_model.get_layer( index=17 ).output
vmodel=GlobalAveragePooling2D()(vmodel)
vmodel=Dense(256, activation='relu')(vmodel)                          
vmodel=Dropout(0.5)(vmodel)
vmodel=Dense(1, activation='sigmoid')(vmodel)                           
                           
                           
                           
model1 = Model(inputs=base_model.input, outputs=vmodel) 
'''

for i, layer in enumerate(base_model.layers):
   print(i, layer.name)
   
#print(base_model.input_shape)
   
''' 
base_model =VGG16(include_top=False,weights= 'imagenet') 
vmodel=base_model.get_layer( index=17 ).output
vmodel=GlobalAveragePooling2D()(vmodel)
vmodel=Dense(256, activation='relu')(vmodel)                          
vmodel=Dropout(0.5)(vmodel)
vmodel=Dense(1, activation='sigmoid')(vmodel)                           
                           
                           
                           
model1 = Model(inputs=base_model.input, outputs=vmodel) 

model=Sequential()
model.add(model1)
for i, layer in enumerate(model.layers):
   print(i, layer.name)
   
k=model1.get_layer( index=18 ).input_shape
print(k)
'''                     
