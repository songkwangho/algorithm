# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 10:18:43 2018

@author: admin
"""

def fact(k):
    tmp=1
    for t in range(1,k+1):
        tmp*=t
    return tmp

i = int(input())
print(fact(i))