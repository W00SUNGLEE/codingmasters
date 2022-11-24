# Floyd-Warshall
import sys

n, start, end, m = map(int, sys.stdin.readline().split())

tmp_list = list()

for _ in range(m):
    tmp_list.append(list(map(int, sys.stdin.readline().split())))

cpu_efficiency = list((map(int, sys.stdin.readline().split())))

graph = dict()

for i in range(n):
    graph[i] = dict()

for i in range(m):
    graph[tmp_list[i][0]][tmp_list[i][1]] = cpu_efficiency[tmp_list[i][1]] - tmp_list[i][2]

def bf(start):
    distances = dict()

    for node in graph:
        distances[node] = -sys.maxsize

    distances[start] = 0

    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                if distances[neighbor] < distances[node] + graph[node][neighbor]:
                    distances[neighbor] = distances[node] + graph[node][neighbor]

    new_distances = dict()

    for node in graph:
        new_distances[node] = distances[node]

    new_distances[start] = 0

    for i in range(len(graph) - 1):
        for node in graph:
            for neighbor in graph[node]:
                if new_distances[neighbor] < new_distances[node] + graph[node][neighbor]:
                    new_distances[neighbor] = new_distances[node] + graph[node][neighbor]

    return distances, new_distances

distances, new_distances = bf(start)

if distances[end] == -sys.maxsize:
    print("INCOMPLETE")

else:
    if distances[end] < new_distances[end]:
        print("INF")

    else:
        print(cpu_efficiency[start] + distances[end])