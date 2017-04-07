#!/usr/bin/python3

p,q = map(int, input().split())

numbers = []
for n in range(p,q+1):
    nsqr = n**2
    strn = str(nsqr)
    k = len(strn)
    rh = (k // 2) + (k & 1) if k > 1 else 1
    lh = k - rh
    strr = strn[-rh:]
    strl = strn[:lh]
    r = int(strr) 
    l = int(strl) if strl else 0
    if l + r == n: 
        numbers.append(n)

if numbers:
    for i in numbers:
        print(i, end=" ")
    print()
else:
    print("INVALID RANGE")

