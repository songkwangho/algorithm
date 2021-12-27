# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:31:55 2018

@author: admin
"""
def DFS(graph,st_node):
    s_stk=[st_node]    
    rt_lst=[st_node] 
    while len(s_stk)>0:
        child=sorted(set.difference(set(graph[s_stk[len(s_stk)-1]]),set(rt_lst)))
        if len(child)>0:#자식 있으면             
            rt_lst.append(child[0])
            s_stk.append(child[0])                
            
        else:#자식 없으면
            s_stk.pop()
            
    return rt_lst

def BFS(graph,st_node):
    s_que=[st_node]
    rt_lst=[st_node]
           
    while len(s_que)>0:
        temp=s_que.pop(0)    
        child=sorted(set.difference(set(graph[temp]),set(rt_lst)))#아직 안가본 자식들 
        if temp not in rt_lst:#현재 vertex에 처음 왓을때
                rt_lst.append(temp)
        if len(child)>0:#자식 있으면 
            for i in list(child):
                s_que.append(i)
                rt_lst.append(i)
               
    return rt_lst

N,M,V=map(int,input().split(' '))
edge_lst_1=[list() for i in range(N+1)]
edge_lst_2=[list() for i in range(N+1)]
for i in range(M):
    fr,to=map(int,input().split(' '))
    if to not in edge_lst_1[fr]:
        edge_lst_1[fr].append(to)
        edge_lst_1[to].append(fr)
        edge_lst_2[fr].append(to)
        edge_lst_2[to].append(fr)

dfs=DFS(edge_lst_1,V)
for i in dfs:
    print(i,end=' ')
print()    
bfs=BFS(edge_lst_2,V)
for j in bfs:
    print(j,end=' ')