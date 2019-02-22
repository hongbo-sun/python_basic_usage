# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 22:32:36 2017

@author: hongb
"""

from sklearn.metrics import precision_score,recall_score
a=[1,0,1]

b=[1,0,0]
c=precision_score(a,b)
d=recall_score(a,b)
print(c,d)