import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    matrix[a][b] = c

start, end = map(int, sys.stdin.readline().split())

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

answer = distances[end]

print(answer)