# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 10:15:15 2018

@author: admin
"""

def fact(N):
    tmp=1
    for i in range(1,N+1):
        tmp*=i
    return tmp

N=int(input())
k=str(fact(N))

cnt=0
for idx in range(len(k)-1,0,-1):
    if k[idx]==str(0):
        cnt+=1
    else:
        break
print(cnt)