#!/usr/bin/python3

import sys

n = int(input().strip())
c = list(map(int, input().split()))

count = 0
while c:
    temp = c.pop(0)
    try:
        index = c.index(temp)
    except ValueError:
        continue
    _ = c.pop(index)
    count += 1

print(count)
