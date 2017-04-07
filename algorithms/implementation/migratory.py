#!/usr/bin/python3

from collections import Counter

n = int(input())
types = list(map(int, input().split()))
# your code goes here

c = Counter(types)
d = c.most_common(1)
print(d[0][0])
