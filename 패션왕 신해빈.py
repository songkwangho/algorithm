# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:09:22 2018

@author: admin
"""

T=int(input())
for i in range(T):
    n=int(input())
    clothes=dict()
    for j in range(n):
        name,tp= input().split(' ')
        if tp in clothes.keys():
            clothes[tp].append(name)
        else:
            clothes[tp]=[name]
    tmp=1
    for key in clothes.keys():
        tmp*=(len(clothes[key])+1)
    print(tmp-1)