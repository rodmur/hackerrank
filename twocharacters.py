#!/usr/bin/python3

from itertools import combinations
import re, sys

s_len = int(input())
s = input().strip()

S = set(s)
lS = len(S)

if lS < 2:
    print(0)
    sys.exit(0)

F = list(combinations(S, lS - 2))
lengths = []
for x in F:
    s_t = s[:]
    for y in x:
        s_t = s_t.replace(y,'')
    p = list(S - set(x))
    regex = p[1]+r'?('+p[0]+p[1]+r')+|'+p[0]+r'?('+p[1]+p[0]+r')+' 
    pattern = re.compile(regex)
    match = pattern.fullmatch(s_t)
    if match:
        lengths.append(len(s_t))
        
if lengths:
    print(max(lengths))
else:
    print(0)

