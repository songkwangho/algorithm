# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:19:31 2020

@author: admin
"""

num=int(input())
count=0
new_num=num
while True:
    count+=1
    left=new_num//10
    right=new_num%10    
    new_num=right*10+(left+right)%10
    if new_num==num:
        break
    else:
        new_num=right*10+new_num%10
print(count)            