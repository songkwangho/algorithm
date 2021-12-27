# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:55:33 2018

@author: admin
"""

N=int(input())
selec=list()
DP=[[0,0,0] for i in range(N)]
prev=-1
for k in range(N):
    R,G,B=map(int,input().split(' '))
    selec.append([R,G,B])
    if prev==-1:
        DP[k]=[R,G,B]
        prev=0
    elif prev==0:
        DP[k][0]=R+min([DP[k-1][1],DP[k-1][2]])
        DP[k][1]=G+min([DP[k-1][0],DP[k-1][2]])
        DP[k][2]=B+min([DP[k-1][0],DP[k-1][1]])

score=min(DP[N-1])
print(score)

#    if prev==-1:
#        m=min([R,G,B])
#        selec.append(m)
#        prev=[R,G,B].index(m)
#    elif prev==0:
#        m=min([1001,G,B])
#        selec.append(m)
#        prev=[1001,G,B].index(m)
#    elif prev==1:        
#        m=min([R,1001,B])
#        selec.append(m)
#        prev=[R,1001,B].index(m)
#    elif prev==2:
#        m=min([R,G,1001])
#        selec.append(m)
#        prev=[R,G,1001].index(m)