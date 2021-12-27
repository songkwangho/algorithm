# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:36:36 2018

@author: admin
"""

N=int(input())
l_list=[[] for i in range(50)]
for i in range(N):
    S=input()
    l_list[len(S)-1].append(S)

for idx in range(len(l_list)):
    if len(l_list[idx])>1:
        l_list[idx]=set(l_list[idx])
        l_list[idx]=list(l_list[idx])        
        l_list[idx].sort()
        
    if len(l_list[idx])>=1:
        for w in l_list[idx]:
                print(w)
