# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:28:03 2018

@author: admin
"""
def rx_srt(in_lst,max_len):
    for n in range(1,max_len+1):
        count=[[] for i in range(10)]#0-9까지 숫자에 따른 버킷 
        tmp_lst=list()
        for num in in_lst:
            count[int((num%pow(10,n))/pow(10,n-1))].append(num)        
        for lst in count:
            while len(lst)!=0:
                tmp_lst.append(lst.pop(0))
        in_lst=tmp_lst
    return in_lst

N=int(input())
i_data=list()
max_len=0
for i in range(N):
    data=input()
    if len(data)>max_len:
        max_len=len(data)
    i_data.append(int(data))

o_data=rx_srt(i_data,max_len)
for o in o_data:
    print(o)