#!/usr/bin/python3


n = int(input())
c = list(map(int, input().split()))

print (sum(c.count(x)//2 for x in set(c)))
