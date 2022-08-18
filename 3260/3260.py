import sys

n = int(sys.stdin.readline())

while True:
    n += 1

    if n / 2 % 2 == 1:
        print(n)
        break