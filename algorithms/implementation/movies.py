#!/usr/bin/python3

i,j,k = map(int, input().split())

count = 0
for x in range(i,j+1):
    rx = int(str(x)[::-1])
    if abs(x-rx) % k == 0:
        count += 1

print(count)
