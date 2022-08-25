import sys

N, A, B, C = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

aircondition = list()

for _ in range(A):
    x, y = map(int, sys.stdin.readline().split())

    aircondition.append((x, y))

    for i in range(x-B, x+B+1):
        if 0 < i <= N:
            matrix[i][y] += 1

    for i in range(y-B, y+B+1):
        if 0 < i <= N:
            matrix[x][i] += 1

for x, y in aircondition:
    matrix[x][y] = -1

answer = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if matrix[i][j] >= C:
            answer += 1

print(answer)