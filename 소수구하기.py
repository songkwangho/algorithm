# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:13:29 2018

@author: admin
"""

def is_prime(N):
    k=int(pow(N,0.5))
    if N>1:
        if N%2==0:
            return N==2
        else:
            for i in range(3,k+1):
                if N%i==0:
                    return False
            return True               
    else:
        return False

M,N=map(int,input().split(' '))
for t in range(M,N+1):
    if is_prime(t):
        print(t)
        