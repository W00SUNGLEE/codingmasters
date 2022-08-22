import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

answer = sum(arr)

if answer < 100:
    print(100 - answer)

else:
    print(0)