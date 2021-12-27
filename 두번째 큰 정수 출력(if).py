# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:58:30 2018

@author: admin
"""
a,b,c=map(int,input().split())
if a>=b>=c or a<=b<=c:
    print(b)  
elif c>=a>=b or c<=a<=b:
    print(a)
elif a<=c<=b or a>=c>=b:
    print(c)