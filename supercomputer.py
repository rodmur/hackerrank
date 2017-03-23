#!/usr/bin/python3

from copy import deepcopy

def findcross(n,m,c,grid,cross):
    candidates = []
    for k in range(c):
        for i in range(n):
            for j in range(m):
                ok = True
                for x,y in cross[k]:
                    if 0 <= i+x < n and 0 <= j+y < m and grid[i+x][j+y] == 'G':
                        pass
                    else:
                        ok = False
                        break
                
                if ok:
                    candidates.append((i,j,k))

    return candidates
                
                
n,m = map(int, input().split())

grid = []
for _ in range(n):
    line = list(input().strip())
    grid.append(line)
    
c = min(n,m)
cross = []
for i in range(c):
    cross.append([])
    for j in range(0,i+1):
        cross[i].append((j,0))
        if j == 0:
            continue
        cross[i].append((0,j))
        cross[i].append((-j,0))
        cross[i].append((0,-j))
        
cross.reverse()        

cans1 = findcross(n,m,c,grid,cross)

areas = []
for c1 in cans1:
    newgrid = deepcopy(grid)
    i,j,k = c1
    for x,y in cross[k]:
        newgrid[i+x][j+y] = 'B'

    cans2 = findcross(n,m,c,newgrid,cross) 
    for _,_,q in cans2: 
        areas.append(len(cross[k])*len(cross[q]))

print(max(areas))
