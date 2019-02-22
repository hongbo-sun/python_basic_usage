# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:38:52 2017

@author: hongb
"""
'''#测试函数使用
import class_funtion_array_list
num=class_funtion_array_list.add(3,6)
print(num)
'''

#测试类使用
from class_funtion_array_list import myclass
from class_funtion_array_list import add
k=myclass(7,7)
k1=myclass(5,10)
k1.a=k.a+2
a=k.a
b=k.b
c=k.doc
huanying=k.f()
print(huanying)
print (a,b)
print(c)
print(k.a)
print(k1.a)
kk=add(5,6)
print(kk)