import sys
import heapq

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for i in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

start = [-1, -1]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            start = [i, j]
            break

    if sum(start) != -2:
        break

dp = [[sys.maxsize for _ in range(m)] for _ in range(n)]

queue = list()

heapq.heappush(queue, (0, start[0], start[1]))

dp[start[0]][start[1]] = 0

answer = -1

while queue:
    cost, x, y = heapq.heappop(queue)

    if matrix[x][y] == "E":
        answer = cost
        break

    if cost > dp[x][y]:
        continue

    else:
        for xi, yi in move:
            new_x = x + xi
            new_y = y + yi

            if 0 <= new_x < n and 0 <= new_y < m:
                if matrix[new_x][new_y] == 'O':
                    if cost+1 < dp[new_x][new_y]:
                        dp[new_x][new_y] = cost+1
                        heapq.heappush(queue, (cost+1, new_x, new_y))

                elif matrix[new_x][new_y] == 'X' or matrix[new_x][new_y] == 'E':
                    if cost < dp[new_x][new_y]:
                        dp[new_x][new_y] = cost
                        heapq.heappush(queue, (cost, new_x, new_y))

print(answer)