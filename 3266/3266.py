import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    if n % 2 == 0:
        print("R")

    else:
        print("L")