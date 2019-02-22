# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 16:01:08 2018

@author: hongb
"""

def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 




for n in fab(5): 
    print(n)
