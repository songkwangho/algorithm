# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:01:09 2018

@author: admin
"""
N=int(input())
DP=[N for i in range(N+1)]
for k in range(N,0,-1):
    if k==N:
        DP[k]=0
    elif k==N-1:
        DP[k]=1
    else:
        if 2*k<=N and DP[k]>DP[2*k]+1:
            DP[k]=DP[2*k]+1
        if 3*k<=N and DP[k]>DP[3*k]+1:
            DP[k]=DP[3*k]+1
        if DP[k]>DP[k+1]+1:
            DP[k]=DP[k+1]+1
print(DP[1])