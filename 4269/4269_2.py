import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

deq = deque()

deq.append([0, 0, 1, 1])

answer = -1

while deq:
    x, y, skill, count = deq.popleft()

    if x == n-1 and y == m-1:
        answer = count
        break

    for xi, yi in move:
        new_x = x + xi
        new_y = y + yi

        if 0 <= new_x < n and 0 <= new_y < m:
            if matrix[new_x][new_y] == '0':
                matrix[new_x][new_y] = '2'
                deq.append([new_x, new_y, skill, count+1])

            elif matrix[new_x][new_y] == '1' and skill == 1:
                deq.append([new_x, new_y, skill-1, count+1])

print(answer)