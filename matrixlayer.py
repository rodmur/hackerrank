#!/usr/bin/python3

def getshell(i,j,m,n,A):
    strip = []
    for k in range(i,m-i-1):
        strip.append(A[k][j])
    for k in range(j,n-j-1):
        strip.append(A[m-i-1][k])
    for k in range(m-i-1,i,-1):
        strip.append(A[k][n-j-1])
    for k in range(n-j-1,j,-1):
        strip.append(A[i][k])
    return strip

def putshell(i,j,m,n,A,strip):
    s = 0

    for k in range(i,m-i-1):
        A[k][j] = strip[s]
        s += 1
    for k in range(j,n-j-1):
        A[m-i-1][k] = strip[s]
        s += 1
    for k in range(m-i-1,i,-1):
        A[k][n-j-1] = strip[s]
        s += 1
    for k in range(n-j-1,j,-1):
        A[i][k] = strip[s]
        s += 1

    return A

m,n,r = map(int, input().split())
A = []

for _ in range(m):
    row = list(map(int, input().split()))
    A.append(row)


i=j=0
tmpm = m
tmpn = n

while tmpm > 1 and tmpn > 1:
    cells = 2*(tmpm+tmpn) - 4
    steps = r % cells 
    blah = getshell(i,j,m,n,A)
    foo = blah[-steps:] + blah[:-steps]
    nar = putshell(i,j,m,n,A,foo)
    i += 1
    j += 1
    tmpm -= 2
    tmpn -= 2


for i in range(m):
    for j in range(n):
        print(A[i][j],end=" ")
    print()
