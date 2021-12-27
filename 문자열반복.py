# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 17:14:37 2018

@author: admin
"""

T=int(input())
input_lst=list()
for i in range(T):
    in_lst=input().split(' ')
    R=int(in_lst[0])
    S=in_lst[1]
    input_lst.append([R,S])
for inputdata in input_lst:
    for c in inputdata[1]:
        for i in range(inputdata[0]):
            print(c,end='')
    print('')       
    