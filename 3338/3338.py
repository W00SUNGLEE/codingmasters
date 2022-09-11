import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

n = 3

matrix = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1]]

matrix2 = [[[[0, 1, 0],
            [1, 1, 0],
            [0, 0, 0]],
           [[1, 0, 1],
            [1, 1, 1],
            [0, 0, 0]],
           [[0, 1, 0],
            [0, 1, 1],
            [0, 0, 0]]],
           [[[1, 1, 0],
             [0, 1, 0],
             [1, 1, 0]],
            [[1, 1, 1],
             [1, 0, 1],
             [1, 1, 1]],
            [[0, 1, 1],
             [0, 1, 0],
             [0, 1, 1]]],
           [[[0, 0, 0],
             [1, 1, 0],
             [0, 1, 0]],
            [[0, 0, 0],
             [1, 1, 1],
             [1, 0, 1]],
            [[0, 0, 0],
             [0, 1, 1],
             [0, 1, 0]]]]

matrix3 = [[[[0, 0, 1],
            [0, 0, 1],
            [1, 1, 1]],
           [[0, 0, 0],
            [0, 0, 0],
            [1, 1, 1]],
           [[1, 0, 0],
            [1, 0, 0],
            [1, 1, 1]]],
           [[[0, 0, 1],
             [0, 0, 1],
             [0, 0, 1]],
            [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]],
            [[1, 0, 0],
             [1, 0, 0],
             [1, 0, 0]]],
           [[[1, 1, 1],
             [0, 0, 1],
             [0, 0, 1]],
            [[1, 1, 1],
             [0, 0, 0],
             [0, 0, 0]],
            [[1, 1, 1],
             [1, 0, 0],
             [1, 0, 0]]]]

for index in range(len(arr)):
    if arr[index] == 2:
        tmp_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(n):
            for j in range(n):
                for a in range(n):
                    for b in range(n):
                        tmp_matrix[a][b] += matrix[i][j] * matrix2[i][j][a][b]
                        if tmp_matrix[a][b] >= 1000000007:
                            tmp_matrix[a][b] -= 1000000007

        matrix = tmp_matrix

    elif arr[index] == 3:
        tmp_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(n):
            for j in range(n):
                for a in range(n):
                    for b in range(n):
                        tmp_matrix[a][b] += matrix[i][j] * matrix3[i][j][a][b]
                        if tmp_matrix[a][b] >= 1000000007:
                            tmp_matrix[a][b] -= 1000000007

        matrix = tmp_matrix

    else:
        continue

answer = 0

for i in range(n):
    for j in range(n):
        answer += matrix[i][j]

print(answer%1000000007)