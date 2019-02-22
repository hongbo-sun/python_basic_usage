# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 09:02:44 2017

@author: hongb
"""

from numpy import *

import tensorflow as tf




#tf求梯度

w1 = tf.Variable([[1,2]])  
w2 = tf.Variable([[3,4]])  

res = tf.matmul(w2, [[2],[1]])  

grads = tf.gradients(res, w2)  

with tf.Session() as sess:  
    tf.global_variables_initializer().run()
    print (sess.run(res))
    print (sess.run(grads)) 
    
    
import tensorflow as tf
# 注意， bias1 的定义方式
with tf.variable_scope('v_scope') as scope1:
    Weights1 = tf.get_variable('Weights', shape=[2,3])
#     bias1 = tf.Variable([0.52], name='bias')

# 下面来共享上面已经定义好的变量
# note: 在下面的 scope 中的get_variable()变量必须已经定义过了，才能设置 reuse=True，否则会报错
with tf.variable_scope('v_scope', reuse=True) as scope2:
    Weights2 = tf.get_variable('Weights')
    bias2 = tf.Variable([0.52], name='bias')




print (Weights1)
print (Weights2.name)
print (bias2)
print(z)
#print (bias2.name)


    
    
'''
a = mat([[1,2],[3,4]])
b = mat([[1,2],[1,2]])
print(a*b)
print(dot(a,b))
print(multiply(a,b))


a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[1,2]])
print(a.dot(b))

'''

