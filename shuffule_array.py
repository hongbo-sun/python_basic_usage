# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
import tensorflow as tf
import keras

a=np.asarray([[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]])

index=[i for i in range(4)]
print (index)
print

for j in range(5):
    random.shuffle(index )
    print(index)
    


a=a[index]
print(a)


t1 =np.array( [[1.1,2.,3.], [4.,5.,6.]])
t2 = np.array([[7.,8.,9.], [10.,11.,12.]])
t3 = np.array([[15.,8.,9.], [10.,11.,12.]])
c=tf.concat([t1, t2,t3],-1)
print(c) 
with tf.Session():  
    d=c.eval()
    
print(d)

'''
e=keras.layers.concatenate([t1, t2,t3])
print(e) 
with tf.Session():  
    f=e.eval()
    
print(f)
'''