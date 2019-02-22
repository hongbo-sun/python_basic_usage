# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:39:45 2018

@author: hongb
"""

def debug(func):
    def wrapper(*args):  # 把指定参数变为可变参数和关键字参数
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args)
    return wrapper  # 回调包装过的函数

@debug
def say_hello(A):
    print("Hello world!{}".format(A))
    
say_hello('Mr.hou')


