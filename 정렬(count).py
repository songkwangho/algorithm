# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:14:50 2018

@author: admin
"""

#sys.stdin.readline()

N=int(input())

mx_val=0
count=[0 for i in range(10001)]

for i in range(N):
    num=int(input())
    count[num]+=1
    if mx_val<num:
        mx_val=num

for t in range(mx_val+1):
    if count[t]!=0:
        for k in range(count[t]):
            print(t)
            
#def ct_srt(in_lst):
#    count=[0 for i in range(max(in_lst)+1)]#0-9까지 숫자에 따른 버킷 
#    for num in in_lst:
#        count[num]+=1
#        
#    for i in range(1,len(count)):
#        count[i]=count[i]+count[i-1]
#                
#    tmp_lst=[0 for i in range(len(in_lst))]  
#             
#    for num in in_lst:
#        tmp_lst[count[num]-1]=num
#        count[num]-=1
#    
#    return tmp_lst
#
#N=int(input())
#i_data=list()
#for i in range(N):
#    i_data.append(int(input()))
#
#o_data=ct_srt(i_data)
#for o in o_data:
#    print(o)