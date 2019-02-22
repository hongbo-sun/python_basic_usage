# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 23:44:46 2017

@author: hongb
"""
import numpy as np

def by_three(x):
  return x % 3 == 0
print (by_three(15))
threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print (threes_and_fives)
a=[2,3]
(e,f)=list(a)
print(e)
a=[1,[2,3]]
b=[3,4]
c=[a,b]

print (a[-1][-1])
name=['ss,ddd','s','\nk','dd']
print (name)

#np.savetxt('1.csv', name, fmt="%s",delimiter=',',newline='\n')
print ("\n")
a=np.array([[1,2]])
b=np.array([[3],[4]])
c=a.dot(b)
print (c[-1,-1])
