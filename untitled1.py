# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 00:25:19 2017

@author: hongb
"""
'''
def addspam(fn):
    def new(*args):
        print "spam,spam,spam"
        return fn(*args)
    return new
@addspam
def useful(a,b):
    print a**2+b**2
   
a=useful(4,3)
print a
'''



'''
def funA(a):
    print 'funA'

def funB(b):
    print 'funB'
@funA
@funB
def funC():
    print 'funC'
'''



'''
for number in range(5):
  print number,
'''
  
  
''' 
a=["sss",[33434.4],[34,5]]
print a[2][1]
'''







from keras import layers
from keras.layers import Dense
layer = Dense(32)
config = layer.get_config()
reconstructed_layer = Dense.from_config(config)
config = layer.get_config()
layer = layers.deserialize({'class_name': layer.__class__.__name__,'config': config})