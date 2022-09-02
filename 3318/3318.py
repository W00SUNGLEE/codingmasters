import sys

n = int(sys.stdin.readline())

matrix = list()

answer = 0

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    row = True
    column = True

    for j in range(n):
        if matrix[i][j] == 1:
            row = False

        if matrix[j][i] == 1:
            column = False

    if row:
        for j in range(n):
            matrix[i][j] = 0

    if column:
        for j in range(n):
            matrix[j][i] = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            answer += 1

print(answer)