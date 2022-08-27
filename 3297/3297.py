import sys

x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())

if max(abs(x1-x2), abs(y1-y2)) <= (r1+r2)/2:
    print("YES")
else:
    print("NO")