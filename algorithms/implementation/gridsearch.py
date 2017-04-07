#!/usr/bin/python3

def check_it(G,P,r,c):
    ok = True
    p = 1
    row = r + 1
    while ok and p < len(P) and row < len(G):
        column = G[row].find(P[p],c)
        if column < 0 or c != column:
            ok = False
            break
        p += 1
        row += 1
    if row == len(G) and p < len(P):
        ok = False
    return ok

t = int(input().strip())
for _ in range(t):
    R,C = map(int, input().split())
    G = []
    for _ in range(R):
       G.append(input().strip())
    r,c = map(int, input().split())
    P = []
    for _ in range(r):
       P.append(input().strip())

    position = []
    start = 0
    found = False 
    p = P[0]
    g = 0
    while not found and g < R:
        column = 0
        while not found and column < C:
            try: 
                ctmp = G[g].index(p,column)
                found = check_it(G,P,g,ctmp)
                column += 1
            except ValueError:
                break
                
        g += 1
    
    if found:
        print("YES")
    else:
        print("NO")
