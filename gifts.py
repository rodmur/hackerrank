#!/usr/bin/python3

import sys


t = int(input())
for a0 in range(t):
    prices = []
    b,w = map(int, input().split())
    x,y,z = map(int, input().split())
    orig = b * x + w * y
    white = b * x + w * (x + z)
    black = b * (y + z) + w * y
    print(min(orig, white, black))
