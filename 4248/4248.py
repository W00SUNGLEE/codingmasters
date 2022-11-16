import sys
from collections import deque

n = int(sys.stdin.readline())

open_class_list = [0]

indegree = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp_list = list(map(int, sys.stdin.readline().split()))

    open_class_list.append(tmp_list[0])

    if tmp_list[1] > 0:
        for j in range(2, len(tmp_list)):
            graph[tmp_list[j]].append(i)
            indegree[i] += 1

deq = deque()

completion_list = [0 for _ in range(n+1)]

for i in range(1, n+1):
    if indegree[i] == 0 and open_class_list[i] == 1 and completion_list[i] == 0:
        deq.append(i)
        completion_list[i] = 1

answer = 1

result_list = list()

while True:
    if sum(completion_list) == n:
       break

    answer += 1

    for _ in range(len(deq)):
        subject = deq.popleft()
        result_list.append(subject)

        for i in graph[subject]:
            indegree[i] -= 1

    for i in range(1, n + 1):
        if indegree[i] == 0 and open_class_list[i]%2 == answer%2 and completion_list[i] == 0:
            deq.append(i)
            completion_list[i] = 1

print(answer)