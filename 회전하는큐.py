# -*- coding: utf-8 -*-
"""
Created on Fri May 25 14:26:45 2018

@author: admin
"""
def s_l(lst):
    lst.append(lst.pop(0))
    return lst

def s_r(lst):
    lst.insert(0,lst.pop(-1))
    return lst

N,M=map(int,input().split(' '))
if M<=N:  
    N_lst=[i for i in range(1,N+1)]
    idx_lst=[k[0] for k in zip(map(int,input().split(' ')))]
    
    oper_count=0
    while len(idx_lst)>0:
        if idx_lst[0]!=N_lst[0]:
            i=N_lst.index(idx_lst[0])
            if i>int(len(N_lst)/2):
                while idx_lst[0]!=N_lst[0]:
                    N_lst=s_r(N_lst)
                    oper_count+=1 
                                                         
            else:
                while idx_lst[0]!=N_lst[0]:
                    N_lst=s_l(N_lst)
                    oper_count+=1 
                                      
        else:
            idx_lst.pop(0)
            N_lst.pop(0)
    print(oper_count)