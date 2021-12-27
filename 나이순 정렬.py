# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:19:30 2020

@author: admin
"""

N=int(input())
point_lst=list()
for i in range(N):
    age,name=input().split()
    point_lst.append([int(age),name,i])
point_lst.sort(key=lambda x : (x[0],x[2]))

for i in point_lst:
    print("{} {}".format(i[0],i[1]))