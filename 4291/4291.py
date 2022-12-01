import sys
from itertools import combinations
import copy
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

zero_list = list()
two_list = list()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero_list.append([i, j])

        if matrix[i][j] == 2:
            two_list.append([i, j])

combination_zero = list(combinations(zero_list, 3))

answer = 0

for zero_list in combination_zero:
    tmp_matrix = copy.deepcopy(matrix)

    for i in range(3):
        tmp_matrix[zero_list[i][0]][zero_list[i][1]] = 1

    for two_index in two_list:
        deq = deque()

        deq.append([two_index[0], two_index[1]])

        while deq:
            x, y = deq.popleft()

            for xi, yi in move:
                new_x = x + xi
                new_y = y + yi

                if 0 <= new_x < n and 0 <= new_y < m and tmp_matrix[new_x][new_y] == 0:
                    tmp_matrix[new_x][new_y] = 2
                    deq.append([new_x, new_y])

    tmp_answer = 0

    for i in range(n):
        for j in range(m):
            if tmp_matrix[i][j] == 0:
                tmp_answer += 1

    answer = max(tmp_answer, answer)

print(answer)






