#!/usr/bin/python3

def DFS(G, v, visited):
    S = []
    S.append(v)
    edges = 0

    while S:
        v = S.pop()
        if not visited[v]:
            edges += 1
            visited[v] = True
            for w in G[v]:
                S.append(w)
    return edges - 1

    
q = int(input())
for i in range(q):
    n,m,libCost,roadCost = map(int, input().split())
    if libCost < roadCost:
        print(n*libCost)
        for _ in range(m):
            _ = input()
        continue
        
    graph = { k: [] for k in range(1,n+1) }
    for _ in range(m):
        city_1,city_2 = map(int, input().split())
        graph[city_1] += [city_2]
        graph[city_2] += [city_1]
    
    visited = { k: False for k in range(1,n+1) }
    roads = 0
    libraries = 0
    for vertex in range(1,n+1):
        if not visited[vertex]:
            libraries += 1
            roads += DFS(graph, vertex, visited)

    print(libraries * libCost + roads * roadCost)
