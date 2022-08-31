import sys

n, m = map(int, sys.stdin.readline().split())

matrix = list()
answer_matrix = [[0 for _ in range(m)] for _ in range(n)]

answer = 0

for i in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

a, b = map(int, sys.stdin.readline().split())

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "o":
            for x in range(i-a, i+a+1):
                for y in range(j-a, j+a+1):
                    if 0 <= x < n and 0 <= y < m:
                        if abs(x-i) + abs(y-j) <= a:
                            if matrix[x][y] == "g":
                                answer_matrix[x][y] = 1

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "c":
            for x in range(i-b, i+b+1):
                for y in range(j-b, j+b+1):
                    if 0 <= x < n and 0 <= y < m:
                        if abs(x-i) + abs(y-j) <= b:
                            answer_matrix[x][y] = 0

for a in answer_matrix:
    answer += sum(a)

print(answer)