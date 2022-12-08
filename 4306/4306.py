import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

m, n, k = map(int, sys.stdin.readline().split())

matrix = [[1 for _ in range(m)]for _ in range(n)]
deq = deque()

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    matrix[b][a] = 0

answer = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            answer += 1

            deq.append((i, j))

            matrix[i][j] = 1

            while deq:
                x, y = deq.popleft()

                for move_x, move_y in move:
                    xi = x + move_x
                    yi = y + move_y

                    if (0 <= xi < n and 0 <= yi < m) and matrix[xi][yi] == 0:
                        matrix[xi][yi] = 1
                        deq.append((xi, yi))

print(answer)