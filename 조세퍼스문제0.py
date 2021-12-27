# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:35:45 2018

@author: admin
"""

N,M=map(int,input().split(' '))
lst=[i for i in range(1,N+1)]
tmp=-1
count=0
rst=list()
while len(lst)!=0:
    count+=1
    if count==M:
        count=0
        tmp+=M
        while tmp>=len(lst):
            tmp=tmp-len(lst)
        rst.append(lst.pop(tmp))
        tmp-=1
print("<{}>".format(str(rst).strip('[]')))       