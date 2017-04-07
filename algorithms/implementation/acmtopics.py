#!/usr/bin/python3

from math import log,ceil

n,m = map(int, input().split())
topic = []

for topic_i in range(n):
    topic_t = int(input(),2)
    topic.append(topic_t)

result = []
for i in range(n-1):
    for j in range(i+1,n):
        b = topic[i] | topic[j]
        result.append(bin(b).count('1'))

x = max(result)
print(x)
print(result.count(x))
