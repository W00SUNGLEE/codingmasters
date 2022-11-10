import sys
from collections import defaultdict
import heapq

n, m, k = map(int, sys.stdin.readline().split())

a, b = map(int, sys.stdin.readline().split())

meeting_place_list = list(map(int, sys.stdin.readline().split()))

tmp_list = list(map(int, sys.stdin.readline().split()))

graph_list = [[tmp_list[0], tmp_list[1], tmp_list[2]]]
p = tmp_list[3]

graph = defaultdict(dict)
graph[tmp_list[0]][tmp_list[1]] = tmp_list[2]
graph[tmp_list[1]][tmp_list[0]] = tmp_list[2]

for i in range(1, m):
    u = ((graph_list[i-1][0] % n) * (p % n)) % n + 1
    v = ((graph_list[i-1][1] % n) * (p % n)) % n + 1
    w = ((graph_list[i-1][2] % 1000000) * (p % 1000000)) % 1000000 + 1
    graph_list.append([u, v, w])

    if u in graph and v in graph[u]:
        graph[graph_list[i][0]][graph_list[i][1]] = min(graph_list[i][2], graph[graph_list[i][0]][graph_list[i][1]])
        graph[graph_list[i][1]][graph_list[i][0]] = min(graph_list[i][2], graph[graph_list[i][1]][graph_list[i][0]])

    else:
        graph[graph_list[i][0]][graph_list[i][1]] = graph_list[i][2]
        graph[graph_list[i][1]][graph_list[i][0]] = graph_list[i][2]

def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])

    return distances

a_distances = dijkstra(graph, a)
b_distances = dijkstra(graph, b)

answer = sys.maxsize

for i in range(k):
    if meeting_place_list[i] in a_distances.keys() and meeting_place_list[i] in b_distances.keys():
        answer = min(max(a_distances[meeting_place_list[i]], b_distances[meeting_place_list[i]]), answer)

if answer == sys.maxsize:
    print(-1)

else:
    print(answer)