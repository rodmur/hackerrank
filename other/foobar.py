#!/usr/bin/python3

import re

n = int(input())

for _ in range(n):
    a = input().strip()
    b = input().strip()
    m = re.search(b,a,re.IGNORECASE)
    if m is None:
        print("NO")
    else:
        print("YES")
