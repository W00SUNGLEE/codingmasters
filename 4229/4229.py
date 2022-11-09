import sys
import math

n = int(sys.stdin.readline())

target_list = list()

for _ in range(n):
    target_list.append(list(map(int, sys.stdin.readline().split())))

arctan_list = list()

for i in range(len(target_list)):
    x = target_list[i][0]
    y = target_list[i][1]
    if x == 0:
        arctan_list.append([2, x**2 + y**2, i+1])

    else:
        arctan = math.atan(y/x)

        if arctan >= 0:
            arctan_list.append([arctan, x**2 + y**2, i+1])

        else:
            arctan_list.append([4+arctan, x**2 + y**2, i+1])

arctan_list.sort()

for i in range(len(arctan_list)):
    print(arctan_list[i][2], end=" ")