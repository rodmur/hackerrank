#!/usr/bin/python3

import sys

n = int(input())
d = list(map(int, input().split()))

vector = []
inflect = []

if n == 2:
    print("yes")
    if d[0] > d[1]:
        print("swap 1 2")
    sys.exit(0)

for i in range(1,n):
    if d[i-1] < d[i]:
        vector.append(1)
    else:
        vector.append(-1)

    if i > 1 and vector[i-2] != vector[i-1]:
        inflect.append(i)

print(vector)
print(inflect)

if sum(vector) == n-1:
    print("yes")
    sys.exit(0)

if sum(vector) == -(n-1):
    print("yes")
    print("reverse 1 %d" % n)
    sys.exit(0)

li = len(inflect)

if li == 4:
    if inflect[0] == inflect[1]-1 and inflect[2] == inflect[3]-1:
        inflect = inflect[:1] + inflect[3:]
        li = len(inflect)


if n > 3 and li == 1: 
    print("yes")
    print("swap %d %d" % (inflect[0],inflect[0]+1))
    sys.exit(0)

if li > 2:
    print("no")
    sys.exit(0)

if d[inflect[0]] < d[0] or d[inflect[1]] < d[inflect[0]]: 
    print("no")
    sys.exit(0)
    
print("yes")

total = sum(i for i in vector if i < 0)

if total >= -2:
    print("swap %d %d" % (inflect[0], inflect[1])) 
else:
    print("reverse %d %d" % (inflect[0], inflect[1])) 
