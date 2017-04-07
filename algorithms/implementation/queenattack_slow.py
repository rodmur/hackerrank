#!/usr/bin/python3

import sys


n,k = map(int, input().split())
rQueen,cQueen = map(int, input().split())
# just normalizing for a standard matrix layout, offset from zero
# Column is off by just one.
rQueen = n - rQueen
cQueen -= 1

obstacles = []
for _ in range(k):
    rObstacle,cObstacle = map(int, input().split())
    rObstacle = n - rObstacle
    cObstacle -= 1
    obstacles.append((rObstacle,cObstacle)) 
    
x = rQueen
y = cQueen
rays = [True] * 8
moves = 0
        
for shell in range(1,n):
    ray = 0
    for j in range(-shell,shell+1,shell):
        for k in range(-shell,shell+1,shell):
            if j != 0 or k != 0: 
                if 0 <= x + j < n and 0 <= y + k < n:
                    if (x+j,y+k) in obstacles:
                        rays[ray] = False
                    else:
                        if rays[ray]:
                            moves += 1
                ray += 1
print(moves)
