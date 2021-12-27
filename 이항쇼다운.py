# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:00:07 2018

@author: admin
"""
def comb(n,m):
    upper=1
    under=1
    if n-m<m:
        m=n-m
    for t in range(0,m):
        upper*=(n-t)
        under*=(t+1)
    return int(upper/under)
n,m= map(int,input().split(' '))
while not(n==0 and m==0):
    if m==0 or m==n:
        print(1)
    else:
        print(comb(n,m))
    n,m= map(int,input().split(' '))
