import sys
from collections import deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

student_list = list()
cushion_list = list()

matrix = list()

for i in range(n):

    matrix.append(list(sys.stdin.readline().strip()))
    for j in range(m):
        if matrix[i][j] == 'C':
            student_list.append((i, j))

        if matrix[i][j] == 'P':
            cushion_list.append((i, j))

dist = [[0 for _ in range(len(cushion_list))] for _ in range(len(student_list))]

def getDist(index):
    check_matrix = [[-1 for _ in range(m)] for _ in range(n)]
    deq = deque()

    deq.append((student_list[index][0], student_list[index][1]))
    check_matrix[student_list[index][0]][student_list[index][1]] = 0

    while deq:
        x, y = deq.popleft()

        for xi, yi in move:
            new_x = x + xi
            new_y = y + yi

            if 0 <= new_x < n and 0 <= new_y < m:
                if check_matrix[new_x][new_y] == -1 and matrix[new_x][new_y] != 'X':
                    check_matrix[new_x][new_y] = check_matrix[x][y] + 1
                    deq.append((new_x, new_y))

    for i in range(len(cushion_list)):
        dist[index][i] = check_matrix[cushion_list[i][0]][cushion_list[i][1]]

#
for i in range(len(student_list)):
    getDist(i)

if len(student_list) == 1:
    print(0)
    exit(0)

if len(student_list) > len(cushion_list):
    print(-1)
    exit(0)

def bimatch(N, graph, visited, selected):
    if visited[N]:
        return False
    visited[N] = True

    for num in graph[N]:
        if selected[num] == -1 or bimatch(selected[num], graph, visited, selected):
            selected[num] = N
            return True

    return False

def decision(mid):
    graph = [[] for _ in range(len(student_list))]

    for i in range(len(student_list)):
        for j in range(len(cushion_list)):
            if dist[i][j] != -1 and dist[i][j] <= mid:
                graph[i].append(j)

    selected = [-1] * len(cushion_list)
    for i in range(len(student_list)):
        visited = [False] * len(student_list)
        bimatch(i, graph, visited, selected)

    count = 0
    for i in range(len(selected)):
        if selected[i] > -1:
            count += 1

    return count == len(student_list)

left = 0
right = 10000
answer = -1

while left <= right:
    mid = (left + right) // 2

    if decision(mid):
        answer = mid
        right = mid - 1

    else:
        left = mid + 1

print(answer)