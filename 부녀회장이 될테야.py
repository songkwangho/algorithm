# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 10:26:52 2018

@author: admin
"""

T=int(input())
k=[0 for i in range(T)]#층
n=[0 for i in range(T)]#호
for i in range(T):#입력
    k[i]=int(input())
    n[i]=int(input())

for j in range(T):#출력
    a=k[j]
    b=n[j]
    M=1
    q=1
    for t in range(1,2+a):
        M*=t    
    for p in range(0,a+1):
        q*=(b+p)
    print(int(q/M))