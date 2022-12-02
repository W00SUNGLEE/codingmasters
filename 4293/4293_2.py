import sys
from collections import deque
import heapq
import copy

v, e = map(int, sys.stdin.readline().split())

graph = [[sys.maxsize for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c


def dijkstra(graph, start):
    distances = [sys.maxsize for _ in range(v+1)] # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for i in range(len(graph[current_destination])):
            if graph[current_destination][i] < sys.maxsize:
                new_destination = i
                new_distance = graph[current_destination][i]

                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance
                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances

matrix = [[]]

for i in range(1, v+1):
    matrix.append(dijkstra(graph, i))

answer = sys.maxsize

for i in range(1, v+1):
    deq = deque()

    visited = [1 for _ in range(v+1)]
    visited[0] = 0
    visited[i] = 0

    deq.append((i, 0, copy.deepcopy(visited)))

    while deq:

        index, cost, visited = deq.popleft()

        if sum(visited) == 0:
            answer = min(answer, cost)
            continue

        else:
            for j in range(1, v+1):
                if (j != index) and visited[j] == 1:
                    if matrix[index][j] < sys.maxsize:
                        visited[j] = 0
                        deq.append((j, cost+matrix[index][j], copy.deepcopy(visited)))
                        visited[j] = 1

print(answer)