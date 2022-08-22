import sys

a, b = map(int, sys.stdin.readline().split())
x, y = map(int, sys.stdin.readline().split())

if b > y:
    a += b - y

if a > x:
    print("NO")

else:
    print("YES")