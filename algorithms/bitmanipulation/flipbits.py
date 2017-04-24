#!/usr/bin/python3

T = int(input())
mask = (1 << 32) - 1
for _ in range(T):
    print(int(input()) ^ mask)
