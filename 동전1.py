# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 12:55:51 2018

@author: admin
"""

n,k=map(int,input().split(' '))
coin=list()
coin.append(0)
for i in range(n):
    coin.append(int(input()))

D=[0 for i in range(k+1)]
count=0
for j in range(1,k+1):
    if j%coin[1]==0:
        D[j]+=1
for i in range(2,n+1):
    if coin[i]<=k:
        D[coin[i]]+=1
        for j in range(coin[i]+1,k+1):
            D[j]=D[j-coin[i]]+D[j]
        
print(D[k])