#!/usr/bin/python3

def kill(a,b):
    n = len(a)
    m = len(b)
    d = [[False for col in range(n+1)] for row in range(n+1)]

    d[0][0] = True
    for i in range(n+1):
        for j in range(n+1):
            if i < n and a[i].islower():
                d[i + 1][j] |= d[i][j]
            if i < n and j < m and a[i].upper() == b[j]:
                d[i + 1][j + 1] |= d[i][j]

    print("YES") if d[n][m] else print("NO") 

def main():
    q = int(input())
    for _ in range(q):
        a = input().strip()
        b = input().strip()
        kill(a,b)

    return

if __name__ == "__main__":
    main()

