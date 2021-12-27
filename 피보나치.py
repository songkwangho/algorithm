# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:07:42 2018

@author: admin
"""
#def fib(n):
#    if 1 < n:
#        return fib(n-1)+fib(n-2)
#    elif n==1:
#        return fib(n-1)+1
#    elif n==0:
#        return 0

val=int(input())
lst=[0 for num in range(val+1)]
lst[1]=1
for i in range(2,len(lst)):
    lst[i]=lst[i-1]+lst[i-2]
#print(lst[len(lst)-1])
print(lst)