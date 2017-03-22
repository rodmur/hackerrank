#!/usr/bin/python3

for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    if k != 0 and n % k != 0:
        print(-1)
        continue

    arr = [None] * (n+1) # initialize iterable
    for i in range(1,n+1):
        if arr[i] is None:
            arr[i] = i + k
            arr[i+k] = i

    print(*arr[1:])
