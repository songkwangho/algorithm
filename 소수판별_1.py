# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
N=int(input())
count=0
if N<=100 and N:
    in_lst=list(map(int,input().split(' ')))
    if len(in_lst)==N:
        for temp in in_lst:
           if temp > 1 and temp<=1000:
               if temp==2:
                   count+=1
               elif temp%2 == 0:
                   continue
               else:
                   for t in range(2,int(math.sqrt(temp))+1):
                       if temp%t == 0:
                           break
                   else:
                       count+=1
print(count)