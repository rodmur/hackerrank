#!/usr/bin/python3

import re

n = int(input())
lines = []
for i in range(n):
    line_t = input().strip()
    lines.append(line_t)
    
q = int(input())
for _ in range(q):
    s = input().strip()
    pattern = re.compile(r'\w+' + s + r'\w+')
    count = 0
    for line in lines:
        matches = list(pattern.finditer(line))
        count += len(matches)
    print(count)
