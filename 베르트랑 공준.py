# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:22:55 2018

@author: admin
"""
#sys.stdin.readline()
def is_prime(N):
    k=int(pow(N,0.5))
    if N>1:
        if N%2==0:
            return N==2
        else:
            for i in range(3,k+1):
                if N%i==0:
                    return False
            return True               
    else:
        return False

def prime_gen():
    lst=[0 for i in range(246913)]
    for idx in range(2,len(lst)):
        if is_prime(idx):
            lst[idx]=1
    return lst

p_lst=prime_gen()           
while True:
    N=int(input())
    if N!=0:
        print(sum(p_lst[N+1:(2*N+1)]))
    else:
        break