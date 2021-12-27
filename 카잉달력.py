# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 11:36:42 2018

@author: admin
"""
def gcd(a,b):
    if a!=0 and b!=0 and a>b:
        return gcd(b,a%b)
    elif a!=0 and b!=0 and a<=b:
        return gcd(a,b%a)
    elif a==0 or b==0:
        if a==0:
            return b
        else:
            return a
def swap(a,b):
    return (b,a)
        
T=int(input())
out=list()
for i in range(T):
    M,N,x,y=map(int,input().split(' '))
    g=gcd(M,N)
    end=int((M*N)/g)
    if M>N:
        M,N=swap(M,N)
        x,y=swap(x,y)
    if x>=N: out.append(-1)
    else:
        count=x
        j=x        
        while count < end and j != y:
            j+=M
            count+=M
            if j>N : j=j%N
        if end<count or (j!=y and end==count): out.append(-1)     
        else:
            out.append(count)
        
for p in out:
    print(p)