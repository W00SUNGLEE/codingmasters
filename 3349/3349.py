import sys
import math

n = int(sys.stdin.readline())

x, y = map(int, sys.stdin.readline().split())

min_time = sys.maxsize


for i in range(0, abs(x)+1):
    tmp_time = math.sqrt(((i**2)+(n**2))) / 2
    tmp_time += math.sqrt((abs(x)-i)**2 + y**2)

    if tmp_time < min_time:
        min_time = tmp_time
        answer = i

if x >= 0:
    print(answer)
else:
    print(-(answer))
