import sys

a, b = map(float, sys.stdin.readline().split())

while a <= b:
    print("{:.2f}".format(a), end=" ")
    a += round(0.01, 2)