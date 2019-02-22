# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 19:38:07 2017

@author: hongb
"""





'''#array和列表，array的寻值方式a[1,2,3],list的寻值方式a[1][2][3]
import numpy as np
a=['ssss',[[1,2],
[3,4]],
[[5,6],
[7,9]]]
b=[[[1,2],
[3,4]],
[[5,6],
[7,9]]]
arr = np.asarray(b, dtype="int8")
print(a[0])
print(arr[1,0,0])
'''




#类的练习，__init__(self,参数1，参数2)，进行类的初始化
class myclass:
    doc='A simple example class'
    i = 12345
    a=0
    b=2
    def f(self):
        return 'hello world'
    def __init__(self, realpart=6, imagpart=7):
        self.a=realpart
        self.b=imagpart
if __name__ == '__main__':
    k=myclass()
    k1=myclass(5,10)
    print (k.a,k.b)
    k1.a=k.a+9
    a=k.a
    b=k.b
    c=k.doc
    huanying=k.f()
    print(huanying)
    print ((a,b))
    print(c)
    print(k.a)
    print(k1.b)



'''
#测试函数
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
if __name__ == '__main__':
    print("hello")
    print sub(5,4)
'''