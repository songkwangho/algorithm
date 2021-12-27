# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:45:28 2018

@author: admin
"""
#import sys
#sys.stdin.readline()
#from collections import Counter

def median(in_l):
    return in_l[int(len(in_l)//2)]    

N=int(input())
in_lst=list()
count=[0 for i in range(8001)]
for i in range(N):
    num=int(input())
    in_lst.append(num)
    count[num+4000]+=1

in_lst.sort()

print(round(sum(in_lst)/len(in_lst)))#평균
print(median(in_lst))#중앙값

mx=max(count)
j=0
M=list()
for i in count:
    if i==mx:
        M.append(j-4000)
    j+=1

if len(M)==1:#최빈값 
    print(M[0])
elif len(M)>1:
    print(M[1])
    
#cnt=Counter(in_lst)
#m=cnt.most_common(2)
#if m[0][1]==m[1][1]:
#    k=m[1][0]
#else:
#    k=m[0][0]

print(max(in_lst)-min(in_lst))#범위