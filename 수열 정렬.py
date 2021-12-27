# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 09:55:04 2021

@author: admin
"""
N = int(input())
A=[i for i in map(int, input().split())]

B=sorted(A)
P=list()
for n in A:
    i = B.index(n)
    while i in P:
        s=i+1
        i = B.index(n,s)
    P.append(i)
for p in P:
    print(p, end=" ")
