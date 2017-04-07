#!/usr/bin/python3

N = int(input())
B = list(map(int, input().split()))

cnt = 0
for i in range(N-1):
    if B[i] & 1:
        B[i] += 1
        B[i+1] += 1
        cnt += 2
if B[-1] & 1:
    print("NO")
else:
    print(cnt)

