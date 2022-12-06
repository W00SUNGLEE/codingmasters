import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

deq = deque()

answer = 0
matrix[0][0] = '0'

deq.append((0, 0, 1))

check = True

while deq and check:
    x, y, count = deq.popleft()

    for move_x, move_y in move:
        xi = x + move_x
        yi = y + move_y

        if (0 <= xi < n and 0 <= yi < m) and matrix[xi][yi] == '1':
            if xi == n-1 and yi == m-1:
                answer = count + 1
                check = False
                break

            else:
                matrix[xi][yi] = '0'
                deq.append((xi, yi, count+1))

print(answer)