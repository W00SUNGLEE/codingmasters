import sys

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            matrix[i][j] = -2

answer = 0

check = True

while check:

    check = False

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == answer+1:
                for xi, yi in move:
                    new_x = i + xi
                    new_y = j + yi

                    if 0 <= new_x < n and 0 <= new_y < m:
                        if matrix[new_x][new_y] == 0:
                            matrix[new_x][new_y] = answer + 2
                            check = True

    if check:
        answer += 1

zero_count = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero_count = 1
            break

    if zero_count == 1:
        break

if zero_count == 1:
    print(-1)

else:
    print(answer)