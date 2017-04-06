#!/usr/bin/python3

n = int(input())
line = []
for _ in range(n):
    px,py,qx,qy = map(int, input().split())
    if px >= qx and py >= qy:
        rx = qx - abs(qx - px) 
        ry = qy - abs(qy - py) 
    elif px > qx and py < qy:
        rx = qx - abs(qx - px) 
        ry = qy + abs(qy - py) 
    elif px < qx and py > qy:
        rx = qx + abs(qx - px) 
        ry = qy - abs(qy - py) 
    else:
        rx = qx + abs(qx - px) 
        ry = qy + abs(qy - py) 
        
    print(rx,ry) 
