import sys
from collections import deque

n = int(sys.stdin.readline())

array = deque(sys.stdin.readline().split())

print(" ".join(array))

for _ in range(n-1):
    array.append(array.popleft())
    print(" ".join(array))