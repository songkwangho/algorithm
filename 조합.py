# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:19:00 2018

@author: admin
"""
comb_lst=[[0 for j in range(0,101)] for i in range(0,101)]

def comb():
    comb_lst[1][1]=1
    for k in range(1,101):
        for n in range(k,101):
            if comb_lst[n][k]==0:  
                 if n==k:
                    comb_lst[n][k]=1
                elif k==1:
                    comb_lst[n][k]=n
                else:
                    comb_lst[n][k]=comb_lst[n-1][k-1]+comb_lst[n-1][k]
n,m= map(int,input().split(' '))

comb()
print(comb_lst[n][m])