# -*- coding: utf-8 -*-
"""
Created on Tue May  1 10:26:03 2018

@author: admin
"""

T=int(input())
lst=list()


for i in range(T):
    lst.append(input())
for S in lst:   
    stk=list()
    for s in S:
        if s=='(':
            stk.append(1)
        elif s==')' and len(stk)>0:            
            stk.pop()
        elif s==')' and len(stk)<=0:
            print('NO')
            break
    else:
        if len(stk)>0:
            print('NO')
        else:
            print('YES')