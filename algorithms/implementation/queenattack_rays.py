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

moves = 0

#
# there are 4 lines, 8 rays
#
rays = [(0,-1), (-1,-1), (2,-1), (1,-1), (0,1), (-1,1), (2,1), (1,1)] 

x = rQueen 
y = cQueen

for ray in range(len(rays)):
# m = slope, d = direction, m == 2 is infinity
    m,d = rays[ray]
    for i in range(1,n):
        if m == 0:
            x = rQueen
            if d > 0:
                y = cQueen + i
            else:
                y = cQueen - i
        elif m == -1:
            if d > 0:
                x = rQueen - i
                y = cQueen - i
            else:
                x = rQueen + i
                y = cQueen + i
        elif m == 1:
            if d > 0:
                x = rQueen + i
                y = cQueen - i
            else:
                x = rQueen - i
                y = cQueen + i
        else:
            y = cQueen
            if d > 0:
                x = rQueen + i
            else:
                x = rQueen - i
                
        if 0 <= x < n and 0 <= y < n:
            if (x,y) in obstacles:
                break
            else:
                moves += 1
        else:
            break
print(moves)
