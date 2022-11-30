import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    matrix[a][b] = 1
    matrix[b][a] = 1

min_count = sys.maxsize

for start in range(1+n):
    distances = [sys.maxsize for _ in range(n+1)]
    distances[start] = 0

    queue = list()

    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop((queue))

        if current_distance > distances[current_destination]:
            continue

        for i in range(len(matrix[current_destination])):
            distance = current_distance + matrix[current_destination][i]

            if distance < distances[i]:
                distances[i] = distance
                heapq.heappush(queue, [distance, i])

    distances[0] = 0

    if max(distances) < min_count:
        min_count = max(distances)
        answer = start

print(answer)