#!/usr/bin/python3

def DFS(G, v, visited):
    S = []
    S.append(v)
    edges = 0

    while S:
        v = S.pop()
        if not visited[v]:
            visited[v] = True
            for w in G[v]:
                S.append(w)
        else:
            edges += 1
    return edges 

    
q = int(input())
for i in range(q):
    n,m,x,y = map(int, input().split())
    if x <= y:
        print(n*x)
        for _ in range(m):
            _ = input()
        continue
        
    graph = { k: [] for k in range(1,n+1) }
    for _ in range(m):
        city_1,city_2 = map(int, input().split())
        graph[city_1] += [city_2]
    
    visited = { k: False for k in range(1,n+1) }
    roads = 0
    libraries = 0
    vertex = 1
    while sum(visited.values()) < n:
        roads += DFS(graph, vertex, visited)
        libraries += 1
        for k,v in visited.items():
            if v is False:
                vertex = k
                break

    print(libraries * x + roads * y)
