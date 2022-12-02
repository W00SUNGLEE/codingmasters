import sys
import heapq

sys.setrecursionlimit(10**6)

v, e = map(int, sys.stdin.readline().split())

graph = [[sys.maxsize for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])
    graph[b][a] = min(c, graph[a][b])

start, end = map(int, sys.stdin.readline().split())


def dijkstra(graph, start):
    distances = [sys.maxsize for _ in range(v+1)]
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for i in range(len(graph[current_destination])):
            if graph[current_destination][i] < sys.maxsize:
                new_destination = i
                new_distance = graph[current_destination][i]

                distance = current_distance + new_distance
                if distance < distances[new_destination]:
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])
    return distances

distances_list = dijkstra(graph, start)

answer = distances_list[end]

print(answer)