# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 10:44:48 2020

@author: admin
"""
ans=0
columns=[0 for i in range(16)]#N개의 열, 한 행에는 한개의 퀸만 가능하니까 어딘가 열에 놓엿다면 그때가 행에 놓인것 #입력 가능 N의 크기가 15니까 미리 15짜리 만들어두고 시작
upper_edge=[0 for i in range(31)]#위로 가는 대각선의 좌표 합
downer_edge=[0 for i in range(31)]#아래로 가는 대각선 좌표 차


def queens(linenum, max_num):#colnum = 이번에 퀸 놓을 열의 번호, linenum= 이번에 놓을 행의 번호, max_col=최대 열수 
    global ans
    if linenum>max_num:
        ans+=1
        return
    for c in range(1,max_num+1):  
        if columns[c]==0 and upper_edge[c+linenum]==0 and downer_edge[max_num+(linenum-c)+1]==0:            
            columns[c]+=1
            upper_edge[c+linenum]+=1
            downer_edge[max_num+(linenum-c)+1]+=1
                
            queens(linenum+1, max_num)
                
            columns[c]-=1
            upper_edge[c+linenum]-=1
            downer_edge[max_num+(linenum-c)+1]-=1
    
    return

N=int(input())
queens(1,N)
print(ans)
