# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 10:23:06 2018

@author: admin
"""

def is_prime(N):
    top=int(pow(N,0.5))+1
    if N%2==0:
        return (N==2)
    else:
        for i in range(3,top+1):
            if N%i==0:
                return False
        return True

def prime_gen():
    lst=[False for i in range(10001)]
    for idx in range(2,len(lst)):
        if is_prime(idx):
            lst[idx]=True
    return lst
        
M=int(input())
N=int(input())
p_lst=prime_gen()
r_lst=list()
for k in range(M,N+1):
    if p_lst[k]:
        r_lst.append(k)
        
if len(r_lst)==0:
    print(-1)
else:
    print(sum(r_lst))
    print(min(r_lst))