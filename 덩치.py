# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:32:56 2020

@author: admin
"""

N=int(input())
Persons=list()
for i in range(N):
    A,B = map(int,input().split())
    Persons.append([A,B])

RANK=[' ' for i in range(N)]
for idx,val_i in enumerate(Persons):
    big_one=1
    for jdx,val_j in enumerate(Persons):
            if idx!=jdx:
                if val_i[0]<val_j[0] and val_i[1]<val_j[1]:
                    big_one+=1
    RANK[idx]=str(big_one)
    
print(' '.join(RANK))
            