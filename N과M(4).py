# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:30:39 2020

@author: admin
"""

visited=[0 for i in range(9)]
line=[0 for i in range(9)]

def writing_func(i,N,M):#i = 현재 depth, M= 최대 depth
    if i == M:
        for k in range(M):
            print(line[k],end=" ")
        print("")
        return
    for p in range(1,N+1):#p는 화면에 표시될 숫자 => line에 들어가야지
        visited[i]+=1
        line[i]=p
        if i != 0 and line[i-1]>line[i]:
            visited[i]-=1
        else:
            writing_func(i+1,N,M)
            visited[i]-=1
        
    return 
    
N,M=map(int, input().split())
#N개의 수중에 M개
writing_func(0,N,M)