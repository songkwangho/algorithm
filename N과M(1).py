# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 10:24:22 2020

@author: admin
"""
from itertools import permutations
N,M=map(int, input().split())
perm=permutations([i for i in range(1,N+1)],M)
for item in perm:
    for i in item:
        print(i,end=' ')
    print('',end='\n')

