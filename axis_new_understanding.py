# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 20:20:58 2017

@author: hongb
"""




import numpy as np
a=np.array([[1,2],[3,4]])
b=np.expand_dims(a,axis=0)
print(a.shape)
b=np.expand_dims(a,axis=1)
print(b.shape)
#新发现，axis对应于shape的位置，a.shape=(2,2),b=np.expand_dims(a,axis=0),则b.shape=(1,2,2), 又b=np.expand_dims(a,axis=1)，则b.shape=(2,1,2),可根据此构造b          