#!/usr/bin/python3

import re, string

q = int(input())


for _ in range(q):
    a = input().strip()
    b = input().strip()

    query = ""
    lenb = len(b)
    for i in range(lenb):
        if i < lenb - 1:
            query += r'[%s%s]\w*?' % (b[i].lower(), b[i])
        else:
            query += r'[%s%s]' % (b[i].lower(), b[i])
        
    pattern = re.compile(query)

    m = pattern.search(a)
    if m is None:
        print("NO")
    else:
        print("YES")
