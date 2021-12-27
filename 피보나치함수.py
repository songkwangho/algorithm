# -*- coding: utf-8 -*-
"""
Created on Wed May 30 15:43:44 2018

@author: admin
"""

lst=[0 for num in range(41)]
lst[1]=1
for i in range(2,len(lst)):
    lst[i]=lst[i-1]+lst[i-2]
T=int(input())
for i in range(T):
    N=int(input())
    if N==0:
        print("1 0")
    else:
        print("{} {}".format(lst[N-1],lst[N]))