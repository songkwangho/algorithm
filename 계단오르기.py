# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:43:10 2018

@author: admin
"""

step=list()     
N=int(input())
DP=[[0,0] for i in range(N)]
for k in range(N):
    step.append(int(input()))
    
for i in range(N):
    if i==0:
        DP[i][1]=step[i]
    elif i==1:
        DP[i][0]=DP[i-1][1]
        DP[i][1]=step[i]+max([0,DP[i-1][1]])
    else:
        DP[i][0]=DP[i-1][1]
        DP[i][1]=step[i]+max([DP[i-2][1],DP[i-2][0]+step[i-1]])
print(DP[N-1][1])
