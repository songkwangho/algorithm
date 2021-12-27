# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 13:08:27 2018

@author: admin
"""

def swap(s):
    r=0
    for i in range(3):
       t=s%10
       s=s//10
       r+=t*pow(10,2-i)
    return r

A,B=map(int,input().split(' '))
if swap(A)>swap(B):
    print(swap(A))
else:
    print(swap(B))