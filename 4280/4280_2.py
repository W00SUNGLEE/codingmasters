import sys

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

boomerang_shape = [[[0, 0], [1, 0], [0, 1]],
                   [[0, 1], [0, 0], [1, 1]],
                   [[1, 1], [0, 1], [1, 0]],
                   [[1, 0], [1, 1], [0, 0]]]

answer_list = list()

answer = [0]
tmp = [0]

visited = [[0 for _ in range(m)] for _ in range(n)]

def find_boomerang(i, j, shape_list):
    if visited[i+ shape_list[0][0]][j+shape_list[0][1]] == 0 and visited[i+shape_list[1][0]][j + shape_list[1][1]] == 0 and visited[i + shape_list[2][0]][j + shape_list[2][1]] == 0:
        tmp[0] += matrix[i + shape_list[0][0]][j + shape_list[0][1]] * 2 + matrix[i + shape_list[1][0]][j + shape_list[1][1]] + matrix[i + shape_list[2][0]][j + shape_list[2][1]]
        visited[i + shape_list[0][0]][j + shape_list[0][1]] = 1
        visited[i + shape_list[1][0]][j + shape_list[1][1]] = 1
        visited[i + shape_list[2][0]][j + shape_list[2][1]] = 1
        dfs(i, j)
        visited[i + shape_list[0][0]][j + shape_list[0][1]] = 0
        visited[i + shape_list[1][0]][j + shape_list[1][1]] = 0
        visited[i + shape_list[2][0]][j + shape_list[2][1]] = 0
        tmp[0] -= matrix[i + shape_list[0][0]][j + shape_list[0][1]] * 2 + matrix[i + shape_list[1][0]][j + shape_list[1][1]] + matrix[i + shape_list[2][0]][j + shape_list[2][1]]

def dfs(a, b):
    for j in range(b, m - 1):
        for shape_list in boomerang_shape:
            if 0 <= a + 1 < n and 0 <= j + 1 < m:
                find_boomerang(a, j, shape_list)

    for i in range(a + 1, n - 1):
        for j in range(m - 1):
            for shape_list in boomerang_shape:
                if 0 <= i + 1 < n and 0 <= j + 1 < m:
                    find_boomerang(i, j, shape_list)

    if tmp[0] > answer[0]:
        answer[0] = tmp[0]

dfs(0, 0)

print(answer[0])