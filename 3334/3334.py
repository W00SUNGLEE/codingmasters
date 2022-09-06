import sys
from collections import deque
import copy

string = sys.stdin.readline().strip()

n, m = map(int, sys.stdin.readline().split())

matrix = list()
default_matrix = [["." for _ in range(m)] for _ in range(n)]

queue = deque(list())

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

answer = 0
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == string[0]:
            queue.clear()

            queue.append([0, [i, j], copy.deepcopy(default_matrix)])

            while queue:

                string_index, matrix_index, tmp_matrix = queue.popleft()
                tmp_matrix[matrix_index[0]][matrix_index[1]] = string[string_index]

                if tmp_matrix == matrix:
                    answer += 1
                    break

                if string_index >= len(string) - 1:
                    continue

                else:
                    for x, y in move:
                        xi = x + matrix_index[0]
                        yi = y + matrix_index[1]

                        if 0 <= xi < n and 0 <= yi < m:
                            if tmp_matrix[xi][yi] == "." and matrix[xi][yi] == string[string_index + 1]:
                                queue.append([string_index + 1, [xi, yi], copy.deepcopy(tmp_matrix)])

        else:
            continue

print(answer)