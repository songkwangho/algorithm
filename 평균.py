# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 17:37:37 2020

@author: admin
"""

N=int(input())
cost_lst=[0 for i in range(N)]
for i in range(N):
    rst=input() 
    score=0    
    sum_score=0
    for j,k in enumerate(rst):
        if k=='O':
            score+=1
        else:
            score=0
        sum_score+=score
    cost_lst[i]=sum_score
for c in cost_lst:
    print(c)