# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:57:02 2018

@author: admin
"""

N=int(input())
lst=[0]
for k in range(N):
    s=input()
    if len(s)<2:
        lst.append([int(s)])
    else:
        lst.append(list(map(int,s.split(' '))))
DP=list()
for t in range(1,len(lst)):
    np=len(lst[t])
    tmp=list()
    if np<2:
        DP.append(0)
        DP.append(lst[t])
    else:
        for i in range(0,np):
            if i==0:
                tmp.append(DP[t-1][0]+lst[t][0])
            elif i==(np-1):
                tmp.append(DP[t-1][np-2]+lst[t][np-1])
            else:
                if (DP[t-1][i]+lst[t][i])>(DP[t-1][i-1]+lst[t][i]):
                    tmp.append((DP[t-1][i]+lst[t][i]))
                else:
                    tmp.append((DP[t-1][i-1]+lst[t][i]))
        DP.append(tmp)
print(max(DP[len(DP)-1]))