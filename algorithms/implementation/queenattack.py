#!/usr/bin/python3

n,k = map(int, input().split())
rQ,cQ = map(int, input().split())
# just normalizing for a standard matrix layout, offset from zero
# 
rQ -= 1
cQ -= 1

ray = []
# ray0 
ray.append(cQ)
#ray1
ray.append(min(n-rQ-1, cQ)) 
#ray2
ray.append(n-rQ-1)
#ray3
ray.append(min(n-rQ-1,n-cQ-1))
#ray4
ray.append(n-cQ-1)
#ray5
ray.append(min(rQ, n-cQ-1)) 
#ray6
ray.append(rQ)
#ray7
ray.append(min(rQ, cQ)) 

print("ray: ", ray)

#
# find the lines
# y = mx + b, the four lines we're worried about have slope m = +/-1
# and x = rQ and y = cQ
#

# m = -1
b1 = cQ + rQ
# m = +1
b2 = cQ - rQ


for _ in range(k):
    rB,cB = map(int, input().split())
    rB -= 1
    cB -= 1
#ray0
    if rB == rQ and cB < cQ:
        ray[0] = min(ray[0],cQ - cB - 1)
#ray1
    elif rB == -cB + b1 and rB > rQ and cB < cQ:
        ray[1] = min(ray[1],rB - rQ - 1, cQ - cB - 1)
#ray2
    elif cB == cQ and rB > rQ:
        ray[2] = min(ray[2],rB - rQ - 1)
#ray3
    elif cB == rB + b2 and rB > rQ and cB > cQ:
        ray[3] = min(ray[3],rB - rQ - 1, cB - cQ - 1)
#ray4
    elif rB == rQ and cB > cQ:
        ray[4] = min(ray[4],cB - cQ - 1)
#ray5
    elif cB == -rB + b1 and rB < rQ and cB > cQ:
        ray[5] = min(ray[5],cB - cQ - 1, rQ - rB - 1)
#ray6
    elif cB == cQ and rB < rQ:
        ray[6] = min(ray[6],rQ - rB - 1)
#ray7
    elif cB == rB + b2 and rB < rQ and cB < cQ:
        ray[7] = min(ray[7],cQ - cB - 1, rQ - rB - 1)

print("ray: ", ray)
print(sum(ray))
