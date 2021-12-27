# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 11:02:13 2021

@author: admin
"""
import heapq
from sys import stdin

def dijkstra(start, start_weight):
    distances[start]=start_weight
    queue = list()
    heapq.heappush(queue,(start_weight, start))
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

#N, E = map(int, stdin.readline().split())
N, E = map(int,input().split(' '))
global graph,distances
graph = [list() for n in range(N)] # 0 ~ N-1
distances = [float('inf') for node in graph]

for i in range(E):
    #a, b, c = map(int, stdin.readline().split())#from u to v with weight w
    a,b,c=map(int,input().split(' '))
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))#bi-direction

#v1, v2 = map(int, stdin.readline().split())
v1,v2=map(int,input().split(' '))
dijkstra(0, 0)# index of vertex is same with (Vertex's number - 1) 
  
if distances[v1-1]==float('inf') or distances[v2-1]==float('inf') or distances[N-1]==float('inf'):
    print(-1)
else:
    temp = distances.copy()
    #0->v1->v2->N
    init_=distances[v1-1]
    distances = [float('inf') for node in graph]
    dijkstra(v1-1, init_)
        
    if distances[v1-1]==float('inf') or distances[v2-1]==float('inf') or distances[N-1]==float('inf'):#v1로부터는 v2 또는 N으로 갈수 없음
        distance_path_1 = -1
    else: 
        init_= distances[v2-1]
        distances = [float('inf') for node in graph]
        dijkstra(v2-1, init_)            
        distance_path_1 = -1 if distances[N-1]==float('inf') else distances[N-1]
        
    #0->v2->v1->N
    distances=temp.copy()   
    init_=distances[v2-1]
    distances = [float('inf') for node in graph]
    dijkstra(v2-1, init_)
    
    if distances[v1-1]==float('inf') or distances[v2-1]==float('inf') or distances[N-1]==float('inf'):
        distance_path_2 = -1
    else:    
        init_= distances[v1-1]
        distances = [float('inf') for node in graph]
        dijkstra(v1-1, init_)
        distance_path_2 = -1 if distances[N-1]==float('inf') else distances[N-1]
    
    if distance_path_1>=0 and distance_path_2>=0:
        print(distance_path_1 if distance_path_1<distance_path_2 else distance_path_2)
    elif distance_path_1>=0 and distance_path_2<0: 
        print(distance_path_1)
    elif distance_path_1<0 and distance_path_2>=0: 
        print(distance_path_1)
    else:
        print(-1)



   