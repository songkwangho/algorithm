# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:30:38 2018

@author: admin
"""
#sys.stdin.readline()
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


p_lst=prime_gen()
T=int(input())
in_ist=list()
for i in range(T):
    in_ist.append(int(input()))
    
for n in in_ist:
    t=(int(n/2))
    b=(int(n/2))
    while True:
        if p_lst[b] and p_lst[t]:
            print(b,t)
            if b+t==n:
                print(b,t)
                break
            elif b+t>n:
                t=int(n/2)+(int(n/2)-b)
                b-=1
            elif b+t<n:
                b=int(n/2)-(t-int(n/2))
                t+=1                
        else:
            if b!=0 and not p_lst[b]:
                b-=1
            if t!=len(p_lst) and not p_lst[t]:
                t+=1
