#!/usr/bin/python3

def getstart(m,n,index,r,step):
    i,j = index
# assume m,n are being decrease while access the inner shells
# index is the start point, (0,0), (1,1) etc etc
    
    if step < m:
        row = step 
        col = j
    elif step < m + n - 1:
        row = m - 1
        col = step - m + 1
    elif step < 2*m + n - 2 and m > 2:
        row = m + n - step + 1 if n > 2 else  m + n - step 
        col = n - 1
    elif n > 2:
        row = i
        col = 2*(m+n)-4-step 
    else:
        print("Something has gone really wrong")
        
    return row,col
        
def gettarget(p,q,x,y,i,j):
    if p == i and q < y:
        q += 1
    elif p == x and q > 0:
        q -= 1
    elif p < x and q == j:
        p -= 1
    else:
        p += 1
    return p,q

def getsource(p,q,x,y,i,j):
    


m,n,r = map(int, input().split())
A = []

for _ in range(m):
    row = list(map(int, input().split()))
    A.append(row)

indexi = 0
indexj = 0
x = m
y = n
steps = r % (2*(m+n) - 4)

while x > 1 and y > 1:
    p,q = getstart(x,y, (indexi,indexj), r, steps)
    tmpa = A[p,q]
    for _ in range(steps):
        targeti,targetj = gettarget(p,q,x,y,indexi,indexj)
        sourcei,sourcej = getsource(p,q,x,y,indexi,indexj)
        A[targeti,targetj] = A[sourcei,sourcej]
        
