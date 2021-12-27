# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:09:59 2018

@author: admin
"""

N,X=map(int,input().split(' '))
if N>= 1 and X<=10000:
    num_lst=list(map(int,input().split(' ')))
    remainder=list()
    for num in num_lst:
        if num<X:
            remainder.append(num)
    for num_r in remainder:
        print(num_r,end=" ")