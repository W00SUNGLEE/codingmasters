import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int ,sys.stdin.readline().split())

matrix = list()
deq = deque()

answer = 0

for i in range(n):
    tmp = sys.stdin.readline().strip()

    matrix.append(list())

    for j in range(m):
        matrix[i].append(int(tmp[j]))

for i in range(n):

    for j in range(m):
        if matrix[i][j] == 0:
            answer += 1

            deq.append((i, j))

            while deq:
                x, y = deq.popleft()

                matrix[x][y] = 1

                for move_x, move_y in move:
                    xi = x + move_x
                    yi = y + move_y

                    if (0 <= xi < n and 0 <= yi < m) and matrix[xi][yi] == 0:
                        deq.append((xi, yi))

print(answer)