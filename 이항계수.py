# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 17:32:27 2018

@author: admin
"""

def factorial(num):
    if num>1:
        return num*factorial(num-1)
    else:
        return 1

N,K=map(int,input().split(' '))
if N>=1 and N<=10 and K>=0 and K<=N:
    print(int(factorial(N)/(factorial(K)*factorial(N-K))))