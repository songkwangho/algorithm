# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 18:01:14 2018

@author: admin
"""

class graph:
    def __init__(self):
        self.graph=dict()
    def addEdge(self,u,v):
        if v not in self.graph.keys():
            self.graph[v]={u}
        else:
            self.graph[v].add(u)
    def size(self):
        return len(self.graph.keys())

def search(start):
    global G,DP,D
    s=[start]#start로 오는 애들이 s임,s는 set이고 앞으로 방문할 노드들을 기억할 용도로 쓸것임
    DP[start]=D[start-1]
    leaves=dict()
    while len(s)>0:#더이상 방문할 곳이 없을때까지
        sp=s.pop()#현위치(부모)
        if sp in G.graph.keys():#내가 자식이 있으면
            for t in G.graph[sp]:#모든 자식들을 살펴보는데            
                if DP[t]<0:#t에 온적 없는경우
                    DP[t]=DP[sp]+D[t-1]#t의 비용을 업데이트하고                
                    s.insert(0,t)#t의 자식들을 방문할 수 있도록 set에 추가
                else:#t에 온적 있음
                    if DP[t]<DP[sp]+D[t-1]:#기존에 저장되어 있는 값이 새로운값보다 작으면 
                        DP[t]=DP[sp]+D[t-1]#더 큰값으로 바뀜
                        s.insert(0,t)
        else:#자식이 없으면 리프노드 즉, 시작점임
            leaves[sp]=DP[sp]          
    
    return max(leaves.values())


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
    print(search(W))