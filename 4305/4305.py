import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

def bfs(n, start, matrix):
    deq = deque()
    visited = [0 for _ in range(n)]
    visited[start] = 1

    for i in range(n):
        if matrix[start][i] == 'Y':
            visited[i] = 1
            deq.append(i)

    while deq:
        index = deq.popleft()

        for i in range(n):
            if matrix[index][i] == 'Y' and visited[i] == 0:
                visited[i] = 1
                deq.append(i)

    return sum(visited)-1

answer = 0

for i in range(n):
    score = bfs(n, i, matrix)
    if score > answer:
        answer = score

print(answer)