#!/usr/bin/python3

import sys

n = int(input())
grid = []
output = []
for _ in range(n):
    line = input().strip()
    grid.append(line)

output.append(grid[0])

for i in range(1,n-1):
    output.append(grid[i])
    for j in range(1,n-1):
        p = int(grid[i][j])
        t = int(grid[i-1][j])
        b = int(grid[i+1][j])
        l = int(grid[i][j-1])
        r = int(grid[i][j+1])
        if p > t and p > b and p > l and p > r:
            output[i] = grid[i][:j] + 'X' + grid[i][j+1:]

output.append(grid[n-1]) 
for i in range(n):
    print(output[i])
