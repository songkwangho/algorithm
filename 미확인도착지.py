# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 11:02:13 2021

@author: admin
"""
import heapq
from sys import stdin

def dijkstra(start, start_weight, graph):
    distances = [int(1e9) for node in graph]
    distances[start]=start_weight
    queue = list()
    heapq.heappush(queue,(start_weight, start))
    while bool(queue):
        distance2current_vertice, current_vertice = heapq.heappop(queue) 
        if distances[current_vertice] < distance2current_vertice:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        for next_destination, distance2next_destination in graph[current_vertice].items():
            new_distance = distance2current_vertice + distance2next_destination
            if distances[next_destination] > new_distance:
                distances[next_destination] = new_distance
                heapq.heappush(queue,(new_distance, next_destination))
    return distances

# T = int(stdin.readline())
T = int(input())
for t in range(T):
    #N, E, ND = map(int, stdin.readline().split())
    N, E, ND = map(int,input().split(' '))
    #S, G, H = map(int, stdin.readline().split())
    S, G, H = map(int,input().split(' '))
    graph = {n:dict() for n in range(N)} # 0 ~ N-1

    for i in range(E):
        #a, b, c = map(int, stdin.readline().split())#from u to v with weight w
        a,b,c=map(int,input().split(' '))
        graph[a-1][b-1]=c
        graph[b-1][a-1]=c#bi-
    #print(graph)
    distances_from_S = dijkstra(S-1, 0, graph)     
    distances_from_H = dijkstra(H-1, 0, graph)      
    distances_from_G = dijkstra(G-1, 0, graph) 
    #print(distances_from_S, distances_from_H, distances_from_G)
    candidates=list()
    for i in range(ND):
        #x = int(stdin.readline())
        x=int(input())
        #print(distances_from_S[x-1], (distances_from_S[G-1]+graph[G-1][H-1]+distances_from_H[x-1]),(distances_from_S[H-1]+graph[G-1][H-1]+distances_from_G[x-1]) )
        if G==S:
            if distances_from_S[x-1]==(graph[G-1][H-1]+distances_from_H[x-1]):
                candidates.append(x)            
            else:
                continue
        elif H==S:
            if distances_from_S[x-1]==(graph[H-1][G-1]+distances_from_G[x-1]):
                candidates.append(x)            
            else:
                continue
        else:
            if distances_from_S[x-1]==(distances_from_S[G-1]+graph[G-1][H-1]+distances_from_H[x-1]) or \
                distances_from_S[x-1]==(distances_from_S[H-1]+graph[H-1][G-1]+distances_from_G[x-1]) :
                candidates.append(x)            
            else:
                continue
    candidates.sort()
    print(' '.join(str(x) for x in candidates))        
        




   