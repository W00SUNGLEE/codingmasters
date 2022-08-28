import sys

a, b, D, d = map(int, sys.stdin.readline().split())

min_max_a = [0, 0]

min_max_b = [0, 0]

tmp = a // D
if a % D == 0:
    min_max_a[0] = tmp
else:
    if d * (tmp+1) <= a <= D * (tmp+1):
        min_max_a[0] = tmp+1

tmp = a // d
if d * tmp <= a <= D * tmp:
    min_max_a[1] = tmp

tmp = b // D
if b % D == 0:
    min_max_b[0] = tmp
else:
    if d * (tmp+1) <= b <= D * (tmp+1):
        min_max_b[0] = tmp+1

tmp = b // d
if d * tmp <= b <= D * tmp:
    min_max_b[1] = tmp

if min_max_a[0] > 0 and min_max_a[1] > 0 and min_max_b[0] > 0 and min_max_b[1] > 0:
    print((min_max_a[0]+min_max_b[0])*2, (min_max_a[1]+min_max_b[1])*2)

else:
    print(-1)