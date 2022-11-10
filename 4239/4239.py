import sys
from collections import defaultdict
import heapq

n, q = map(int, sys.stdin.readline().split())

graph = defaultdict(dict)

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

for _ in range(q):
    query = list(map(int, sys.stdin.readline().split()))

    if query[0] == 1:
        graph[query[1]][query[2]] = 1
        graph[query[2]][query[1]] = 1



    elif query[0] == 2:
        person = query[1]
        distances = dijkstra(graph, person)

        friend_list  = list()

        for i in distances.keys():
            if 0 < distances[i] < sys.maxsize:
                friend_list.append(i)

        print(len(set(friend_list) - set(graph[person].keys())))