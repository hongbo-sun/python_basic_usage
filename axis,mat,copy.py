# -*- coding: utf-8 -*-
"""
Created on Tue Aug 08 11:08:30 2017

@author: hongb
"""
import numpy as np
import copy

x=np.asarray([[[ 0,  1,  2],
        [ 3,  4,  5],
        [ 6,  7,  8]],
       [[ 9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]],
       [[18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]]])
x1=x.sum(axis=0)
print(x1)




a=np.asarray([1,2])
b=a.sum(axis=0)   #如果有轴，则axis_max 对应行， 然后axis_middle对应列，axis_min对应相应各点
print(b)



a=np.asarray([1,2])
x = np.expand_dims(a, axis=0)   #相当于加个维数，即最外面加一个中括号
print(x[0,0])





b=np.asarray([[3],[4]])
a=np.mat(a)
b=np.mat(b)
c=b*a
print(c)

#完全复制，复制后的与原本的完全独立
a=[[1,2]]
b=copy.deepcopy(a)
b[0][0]=9
print(a)
print(b)


#如果将三维数组的每一个二维看做一个平面（plane，X[0, :, :], X[1, :, :], X[2, :, :]），三维数组即是这些二维平面层叠（stacked）出来的结果。则（axis=0）表示全部平面上的对应位置，（axis=1），每一个平面的每一列，（axis=2），每一个平面的每一行。