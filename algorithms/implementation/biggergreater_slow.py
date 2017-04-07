#!/usr/bin/python3

from itertools import permutations
t = int(input())

for i in range(t):
    w = input().strip()
    results = [ ''.join(x) for x in permutations(w) ]
    if results[0] != results[1]:
        for j in sorted(results):
            if results[0] < j:
                break
        print(j)
    else:
        print('no answer')
