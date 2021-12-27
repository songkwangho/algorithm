# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:27:34 2020

@author: admin
"""
def decomp_sum(k):
    rst_sum=k
    while k>0:
        rst_sum+=k%10
        k=k//10
    return rst_sum
N=int(input())
gen_lst=[i for i in range(1,N+1)]
num_lst=[decomp_sum(i) for i in gen_lst]

if N in num_lst:
    print(gen_lst[num_lst.index(N)])
else:
    print(0)