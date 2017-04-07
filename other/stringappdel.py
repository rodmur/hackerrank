#!/usr/bin/python3

import sys

s = input().strip()
t = input().strip()
k = int(input())


if abs(len(s) - len(t)) > k:
    print("No")
    sys.exit(0)

for i in range(k,0,-1):
    if s == t[:len(s)] and len(t) - len(s) == i or len(s) == 0:
        break
    s = s[:-1]

if len(t) - len(s) <= i:
    print("Yes")
else:
    print("No")
 
