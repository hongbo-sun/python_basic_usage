# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:45:18 2018

@author: hongb
"""
import time
import tensorflow as tf
# Creates a graph.


t0=time.time()
a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess.run(c))
t1=time.time()


t=t1-t0
print('train costs',t1- t0,'seconds')
