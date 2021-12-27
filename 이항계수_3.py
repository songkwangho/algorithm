# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:23:52 2018

@author: admin
"""

#def power(a,n):
#    if a==0:
#        return 0
#    if n==0:
#        return 1
#    elif n==1:
#        return a    
#    rt=1
#    while n>0:
#        if n%2==1:
#            rt*=a
#        a*=a
#        n=n//2
#    return rt

def power_n_mod(a,n,p):
    rt=1
    while n>0:
        if n%2!=0:
            rt*=a
            rt%=p
        a*=a
        a%=p
        n=n//2
    return rt
    
P=1000000007

N,K=map(int,input().split(' '))
p1=1
p2=1
for i in range(1,N+1):#N팩토리얼
    p1*=i
    p1%=P    
for i in range(1,K+1):#K팩토리얼
    p2*=i
    p2%=P
for i in range(1,N-K+1):#N-K팩토리얼
    p2*=i
    p2%=P
p3=power_n_mod(p2,P-2,P)#페르마의 소정리를 이용하기위해 K!(N-K)!의 p-2승을 구함 
p3%=P
rst=(p1*p3)%P#거기다가 n!을 곱해서 P로 나눈 나머지를 구함 이게 원래수의 나머지와 동일
#페르마의 소정리 참고!
print(rst)