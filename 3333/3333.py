import sys
import copy

n, m, x = map(int, sys.stdin.readline().split())

matrix = list()

answer = ["NO"]

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def sum_matrix(matrix):
    sum = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sum += matrix[i][j]

    return sum

def dfs(matrix, x):
    if sum_matrix(matrix) == x:
        answer[0] = "YES"
        return None

    for i in range(len(matrix)):
        tmp_matrix = copy.deepcopy(matrix)
        tmp_matrix.pop(i)
        dfs(tmp_matrix, x)

    if len(matrix) > 0:
        for j in range(len(matrix[0])):
            tmp_matrix = copy.deepcopy(matrix)
            for i in range(len(matrix)):
                tmp_matrix[i].pop(j)
            dfs(tmp_matrix, x)

dfs(matrix, x)
print(answer[0])



