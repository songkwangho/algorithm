# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 15:12:49 2018

@author: admin
"""

num=int(input())
count=0
for i in range(num):
    str_lst=[0 for i in range(26)]
    in_str=input()
    for i in range(len(in_str)):
        if str_lst[ord(in_str[i])-ord("a")]==0:
            str_lst[ord(in_str[i])-ord("a")]=1
        elif str_lst[ord(in_str[i])-ord("a")]!=0 and in_str[i]==in_str[i-1]:
            str_lst[ord(in_str[i])-ord("a")]+=1
    if sum(str_lst)==len(in_str):
        count+=1
print(count)            
    