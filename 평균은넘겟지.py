# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:09:01 2020

@author: admin
"""

C=int(input())
rst_lst=list()
for i in range(C):
    in_lst=[int(i) for i in input().split()]
    N=in_lst.pop(0)
    avg=sum(in_lst)/len(in_lst)
    tmp_lst=[1 if in_lst[i]>avg else 0 for i,k in enumerate(in_lst)]
    rst_lst.append((sum(tmp_lst)/len(in_lst))*100)
for rst in rst_lst:
    print('{:.3f}%'.format(rst))