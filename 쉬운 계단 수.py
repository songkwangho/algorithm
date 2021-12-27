# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:40:31 2018

@author: admin
"""
numq=[[0 for i in range(10)] for i in range(101)]

for i in range(1,len(numq)):
    if i==1:
        for j in range(len(numq[i])):
            if j>=1:            
                numq[i][j]=1
    else:
        for j in range(len(numq[i])):
            if j<1:            
                numq[i][j]=numq[i-1][j+1]
            elif j>=len(numq[i])-1:
                numq[i][j]=numq[i-1][j-1]
            else:
                numq[i][j]=numq[i-1][j-1]+numq[i-1][j+1]
N=int(input())
print(sum(numq[N])%1000000000)
        
        