import sys

n = int(sys.stdin.readline())

vertex_list = list()

for i in range(n):
    vertex_list.append(list(map(int, sys.stdin.readline().split())))

vertex_list.append(vertex_list[0])
target = list(map(int, sys.stdin.readline().split()))

count = 0

check = False

for i in range(n):
    x, y = target
    xi, yi = vertex_list[i]
    xj, yj = vertex_list[i+1]
    if (x > xi) != (x > xj):
        tmp_y = (yj-yi) * (target[0] - xi) / (xj-xi) + yi

        if y < tmp_y:
            count += 1

        if y == tmp_y:
            check = True
            break

    elif x == xi and x == xj:
        if min(yi, yj) <= y <= max(yi, yj):
            check = True
            break

if check:
    print(1)

else:
    if count % 2 == 0:
        print(0)

    else:
        print(1)