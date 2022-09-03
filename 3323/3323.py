import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    matrix[a][b] = 1

answer = ["NO"]

def bfs(n):
    for i in range(1, n+1):
        queue = deque(list())
        visited = [0 for _ in range(n + 1)]

        if matrix[n][i] == 1:
            queue.append((i, 1))
            visited[n] = 1
            tmp_index = i
            while queue:
                index, count = queue.popleft()

                if visited[index] == 1:
                    continue

                else:
                    visited[index] = 1

                    for i in range(1, n+1):
                        if visited[i] == 0:
                            if matrix[index][i] == 1:
                                queue.append((i, count+1))

                        else:
                            if matrix[index][i] == 1:
                                if i == n and i != tmp_index:
                                    answer[0] = "YES"
                                    break


bfs(n)
print(answer[0])