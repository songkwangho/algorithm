# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 13:13:30 2018

@author: admin
"""
from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[v].append(u)

def cons(num):
    global DP,G,D
    l=G.graph[num][:]
    m=0
    if len(l)==0:#리프노드니까 DP는 해당 건물의 작업시간
        DP[num]=D[num-1]#D는 DP보다 한칸이 적음
        return D[num-1]#리프 노드 건물 짓는 비용 리턴
    #리프노드가 아니면 연결된 애들을 돌면서 리프노드에 도달할수있도록 함수 재귀호출
    for i in l:
        if DP[i]<0:#i번째 건물에 아직 안가본것
            DP[i]=cons(i)#다음 노드로 이동, 리턴값은 이전 노드까지 지은 건물의 비용 값 
        if m<DP[i]:#이전 노드까지 지은 건물 비용값이 현재 m 보다 크면 m을 바꿔줌
            m=DP[i]
    return m+D[num-1]#이전노드까지 지은 건물 비용 최대값 + 현재 건물 비용값 더해서 리턴
    

T=int(input())
for i in range(T):
    N,K=map(int,input().split(' '))
    G=graph()
    
    D=list(map(int,input().split(' ')))
    DP=[-1 for i in range(N+1)]
    for i in range(K):
        FROM,TO=map(int,input().split(' '))
        G.addEdge(FROM,TO)
        
    W=int(input())
    DP[W]=cons(W)
    print(DP[W])
   