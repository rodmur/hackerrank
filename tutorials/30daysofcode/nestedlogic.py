#!/usr/bin/python3

rd,rm,ry = map(int, input().split())
dd,dm,dy = map(int, input().split())

if ry < dy or (ry == dy and rm < dm) or (ry == dy and rm == dm and rd <= dd):
    fine = 0
elif ry == dy and rm == dm and rd > dd:
    fine = 15 * (rd - dd)
elif ry == dy and rm > dm:
    fine = 500 * (rm - dm)
else:
    fine = 10000

print(fine)

