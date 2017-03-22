#!/usr/bin/python3

def printgrid(G):
    for row in G:
        for k in row:
            if k == 0:
                print(".",end="")
            else:
                print("O",end="")
        print()        
    print()
    return

def printnums(G):
    for row in G:
        print(*row)        
    print()
    return

def incrgrid(G,r,c):
    for i in range(r):
        for j in range(c):
            if G[i][j] > 0:
                G[i][j] += 1
    return

r,c,n = map(int, input().split())

G = []
for _ in range(r):
    g_t = list(input().strip())
    t_t = [1 if x=='O' else 0 for x in g_t]
    G.append(t_t)

n = n if n < 8 else n%4 + 4
for secs in range(1,n):
    incrgrid(G,r,c)
    if secs & 1:
        for i in range(r):
            for j in range(c):
                if G[i][j] == 0:
                    G[i][j] = 1

    if secs & 1 == 0:
        for i in range(r):
            for j in range(c):
                if G[i][j] >= 3:
                    for b in range(-1,2):
                        if 0 <= i+b < r:
                            if b == 0:
                                G[i+b][j] = 0
                            else:
                                if G[i+b][j] < 3:
                                    G[i+b][j] = 0
                        if 0 <= j+b < c:
                            if b == 0:
                                G[i][j+b] = 0
                            else:
                                if G[i][j+b] < 3:
                                    G[i][j+b] = 0
printgrid(G)
