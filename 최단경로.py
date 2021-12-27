# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 11:02:13 2021

@author: admin
"""
import heapq
from sys import stdin

def dijkstra(start):
    distances[start]=0
    queue = list()
    heapq.heappush(queue,(0, start))
    while bool(queue):
        distance2current_vertice, current_vertice = heapq.heappop(queue) 
        if distances[current_vertice] < distance2current_vertice:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        for next_destination, distance2next_destination in graph[current_vertice]:
            new_distance = distance2current_vertice + distance2next_destination
            if distances[next_destination] > new_distance:
                distances[next_destination] = new_distance
                heapq.heappush(queue,(new_distance, next_destination))
    return 

V, E = map(int, stdin.readline().split())
K = int(stdin.readline())
global graph, distance
graph = [list() for v in range(V)] # 0 ~ V-1
distances = [float('inf') for node in graph]

for i in range(E):
    u, v, w = map(int, stdin.readline().split())#from u to v with weight w
    graph[u-1].append((v-1,w))

dijkstra(K-1)# index of vertex is same with (Vertex's number - 1)     

for v in distances:
    print("INF" if v==float('inf') else v)