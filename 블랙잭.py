# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 20:42:22 2020

@author: admin
"""

N,M = map(int, input().split())
card_lst=[i for i in map(int, input().split())]
card_lst.sort(reverse=True)
max_V=0
for i in range(len(card_lst)):
    for j in range(i+1,len(card_lst)):        
        for k in range(j+1,len(card_lst)):
            if card_lst[i]+card_lst[j]+card_lst[k]<=M:
                if max_V<card_lst[i]+card_lst[j]+card_lst[k]:
                    max_V=card_lst[i]+card_lst[j]+card_lst[k]
print(max_V)