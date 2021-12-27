# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:40:10 2018

@author: admin
"""

fact_num=[1 for i in range(1001)]
for idx in range(2,len(fact_num)):
    fact_num[idx]=fact_num[idx-1]*idx
N,K=map(int,input().split(' '))
if N>=1 and N<=1000 and K>=0 and K<=N:
    print((int(fact_num[N]//(fact_num[K]*fact_num[N-K])))%10007)