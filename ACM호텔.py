# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 13:33:05 2018

@author: admin
"""
import sys
T=int(input())
for i in range(T):
    H,W,N=map(int,input().split(' '))
    if H>=1 and W<=99 and N>=1 and N<=(H*W):
        if (N//H)<9:
            if (N%H)==0:
                print(str(H)+'0'+str((N//H)))
            else:
                print(str(N%H)+'0'+str((N//H)+1))
        elif (N//H)==9:
            if (N%H)==0:
                print(str(H)+'0'+str((N//H)))
            else:
                print(str(N%H)+str((N//H)+1))
        else:
            if (N%H)==0:
                print(str(H)+str((N//H)))
            else:
                print(str(N%H)+str((N//H)+1))
