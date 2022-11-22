import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

land_list = [0 for _ in range(n*m)]
graph = [dict() for _ in range(n*m)]
land_heap = list()

for i in range(n):
    for j in range(m):
        land_list[m * i + j] = matrix[i][j]
        heapq.heappush(land_heap, (matrix[i][j], m*i+j))

        if i < n-1:
            graph[m * i + j][m * (i+1) + j] = abs(matrix[i][j] - matrix[i+1][j])
            graph[m * (i + 1) + j][m * i + j] = abs(matrix[i][j] - matrix[i + 1][j])

        if j < m-1:
            graph[m*i+j][m*i+j+1] = abs(matrix[i][j] - matrix[i][j+1])
            graph[m * i + j + 1][m * i + j] = abs(matrix[i][j] - matrix[i][j + 1])

visited = [1 for _ in range(n*m)]

cost, index = heapq.heappop(land_heap)

for key, value in graph[index].items():
    heapq.heappush(land_heap, (value, key))

answer = land_list[index]
visited[index] = 0

while sum(visited) != 0:
    cost, index = heapq.heappop(land_heap)

    if visited[index] == 0:
        continue

    else:
        visited[index] = 0
        answer += cost

        for key, value in graph[index].items():
            if visited[key] == 1:
                heapq.heappush(land_heap, (value, key))

print(answer)