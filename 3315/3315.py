import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

matrix = list()

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

queue1 = deque(list())
queue2 = deque(list())

visited = list()

answer = 0

for i in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

a, b = map(int, sys.stdin.readline().split())

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "c":
            visited.clear()
            queue1.append((i, j, 0))

            while queue1:
                x, y, count = queue1.popleft()
                visited.append((x, y))

                if count == b:
                    continue

                for xi, yi in move:
                    newX = x+xi
                    newY = y+yi

                    if (newX, newY) in visited:
                        continue

                    if 0 <= newX < n and 0 <= newY < m:
                        if matrix[newX][newY] == "g":
                            matrix[newX][newY] = "x"
                            queue1.append((newX, newY, count+1))
                        elif matrix[newX][newY] == "c":
                            continue
                        else:
                            queue1.append((newX, newY, count+1))

for i in range(n):
    for j in range(m):

        if matrix[i][j] == "o":
            visited.clear()
            queue2.append((i, j, 0))

            while queue2:
                x, y, count = queue2.popleft()
                visited.append((x, y))

                if count == a:
                    continue

                for xi, yi in move:
                    newX = x+xi
                    newY = y+yi

                    if (newX, newY) in visited:
                        continue

                    if 0 <= newX < n and 0 <= newY < m:
                        if matrix[newX][newY] == "g":
                            matrix[newX][newY] = "s"
                            queue2.append((newX, newY, count+1))
                        elif matrix[newX][newY] == "o":
                            continue
                        else:
                            queue2.append((newX, newY, count+1))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "s":
            answer += 1

print(answer)