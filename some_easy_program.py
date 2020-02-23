# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:58:00 2017

@author: lenovo
"""
import numpy as np
import copy 
def double_first(k):
  n=k
  n[0] = n[0] * 2

numbers = [1, 2, 3, 4]
double_first(numbers)
print (numbers)

print'\n'
list0=[[2,3],[32222,4]]
print'\n'
print 'b',"a"
list1=copy.deepcopy(list0)
list1.append([3])
print list0
print list1

list1.insert(1,list0)
print list1
del list1[1]
print list1
b=list1.pop()
print(b)
print list1

n = [3, 5, 7]
def double_list(x):
  for i in range(0, len(x)):
    x[i] = x[i] * 2
    return x
print double_list(n)



print range(-7,-4)
print(float("-234.4"))



str="Adsds"
print(str.lower())
print(len(str))



#求字符串分数（字符串中每个字母的分数在字典中）
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def scrabble_score(word):
  word=word.lower()
  sco=0
  for i in word:
    sco=sco+score[i]
  return sco
print scrabble_score("word") 



str ="word"
print(str[1:3])
  
  
  
#替换字符串中特定字符为*
def censor(text,word):
  str=""
  i=0
  while i< len(text):
  #for i in range(len(text)):
    if i+len(word)-1<len(text):
      if text[i:i+len(word)]==word:
        for j in range (len(word)):
          str=str+"*"
        i=i+len(word)
        
      else:
        str=str+text[i]
        i=i+1
    else:
      str=str+text[i]
      i=i+1
  return str


str="aaabbbc"
str1="ab"
print censor(str,str1)
print censor("this hack is wack hack", "hack")



#求列表元素中值
def median(li):
  li1=sorted(li)
  if len(li1)%2==0:
      return ((li1[len(li1)/2]+li1[len(li1)/2-1])/2.0)
  else:
      return (li1[(len(li1)-1)/2])
          
print median([2,3,4])

#给列表元素排序，从小到大
def sorted(li):
  li1=copy.deepcopy(li)
  num=len(li1)
  while(num>1):
    for i in range(num-1):
      if li1[i]>li1[i+1]:
        k=li1[i+1]
        li1[i+1]=li1[i]
        li1[i]=k
    num-=1
  return li1 
  
print sorted([2])
  
  
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for i in grades_input:
    print i

    
print_grades(grades) 
print 
print(2,"sss") 



  
  
  
  
  