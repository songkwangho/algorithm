# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:25:04 2018

@author: admin
"""

def d(n):
    count=0      
    for i in range(1,n+1):
        temp=i
        n_lst=[0 for i in range(4)]
        idx=0
        while (i//10)!=0:
            n_lst[idx]=i%10
            i//=10
            idx+=1
        if i%10!=0:
            n_lst[idx]=i%10
        if (n_lst[3],n_lst[2])==(0,0):
            count+=1
        elif n_lst[3]==0 and 105*n_lst[2]+6*n_lst[0]==temp:
            count+=1
    print(count)
    
num=int(input())
if num<=1000:
    d(num)