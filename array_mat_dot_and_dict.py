# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 15:42:01 2017

@author: hongb
"""
#行向量数组的转置还是本身，行向量矩阵的转置就是正常的装置，数组情况下，行向量的点积是行向量模的平方，矩阵下dot就是矩阵相乘
import numpy as np
a=[1,2,3,4]
b=np.asarray(a)
print(b)
print(np.dot(b.T,b))
b=np.mat(b)
print(b)
c=np.dot(b.T,b)
print(c)


print 
#字典
dict = {'Name': 'Zara', 7:'哈哈','Age': 7, 'Class': 'First'};
 
dict['Age'] = 8 # update existing entry
dict['School'] = "DPS School" # Add new entry
 
 
print  dict['Age']
print  dict['School']
print  dict[7]


a=34
b=str(a)
print b