#!/usr/bin/python3

def jumping(c,i,n):
    if i >= n:
        return 1

    if i + 2 < n and not c[i + 2]:
        i += 2
    else:
        i += 1
    j = jumping(c,i,n)
    return j + 1

n = int(input())
c = list(map(int, input().split()))

i = 0

j = jumping(c,i,n)
print(j)
