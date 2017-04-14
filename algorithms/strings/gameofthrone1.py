#!/usr/bin/python3

from collections import Counter 

S = input().strip()

c = Counter(S)

odd = 0
for i in c.values():
    if i & 1:
        odd += 1

if odd > 1: 
    print("NO")
else:
    print("YES")
    
