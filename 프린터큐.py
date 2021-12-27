# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:29:45 2018

@author: admin
"""

#import sys
#sys.stdin.readline()

def prt_q(que,idx_que,num):
    cnt_prt=0
    rt_cnt=0
    while len(que)>0:
        if max(que)!=que[0]:
            que.append(que.pop(0))
            idx_que.append(idx_que.pop(0))
        else:
            cnt_prt+=1
            if num==idx_que[0]:
                rt_cnt=cnt_prt
            que.pop(0)
            idx_que.pop(0)
    return rt_cnt

T=int(input())
rt_lst=list()
for i in range(T):
    N,M=map(int,input().split(' '))
    q=[k for k in iter(map(int,input().split(' ')))]
    idx_q=[i for i in range(len(q))]
    rt=prt_q(q,idx_q,M)
    rt_lst.append(rt)
    
for i in rt_lst:
    print(i)

