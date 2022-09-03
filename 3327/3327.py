import sys
import copy
n = int(sys.stdin.readline())

length = 5

matrix = list()

adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for _ in range(length):
    matrix.append(list(map(int, list(sys.stdin.readline().strip()))))

for _ in range(n):
    tmp_matrix = [[0 for _ in range(length)] for _ in range(length)]

    for i in range(length):
        for j in range(length):
            count = 0
            for x, y in adjacent:
                xi = x + i
                yj = y + j
                if 0 <= xi < length and 0 <= yj < length:
                    if matrix[xi][yj] == 1:
                        count += 1

            if matrix[i][j] == 1:
                if count == 2 or count == 3:
                    tmp_matrix[i][j] = 1
                else:
                    tmp_matrix[i][j] = 0

            else:
                if count == 3:
                    tmp_matrix[i][j] = 1
                else:
                    tmp_matrix[i][j] = 0

    matrix = copy.deepcopy(tmp_matrix)

for line in matrix:
    print("".join(list(map(str, line))))