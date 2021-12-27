# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:23:21 2020

@author: admin
"""

N=int(input())
if N%5==0:
    print(N//5)
elif N%5==1 :
    if N<5:
        print(-1)
    else:
        print(N//5+1)
elif N%5==2:
    if N<10:
        print(-1)
    else:
        print(N//5+2)
elif N%5==3 :
    if N<5:
        print(1)
    else:
        print(N//5+1)
elif N%5==4 :
    if N<5:
        print(-1)
    else:
        print(N//5+2)