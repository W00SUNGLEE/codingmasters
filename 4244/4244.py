import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline())

open_class_list = [0]

indegree = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    tmp_list = list(map(int, sys.stdin.readline().split()))

    if tmp_list[0] > 0:
        for j in range(1, len(tmp_list)):
            graph[tmp_list[j]].append(i)
            indegree[i] += 1

deq = deque()

floor = 1
answer_dic = defaultdict(int)

for i in range(1, n+1):
    if indegree[i] == 0:
        deq.append(i)
        answer_dic[floor] += 1

while deq:
    floor += 1

    for _ in range(len(deq)):
        subject = deq.popleft()

        for i in graph[subject]:
            indegree[i] -= 1

            if indegree[i] == 0:
                deq.append(i)
                answer_dic[floor] += 1

print(len(answer_dic.keys()))
for value in answer_dic.values():
    print(value, end=" ")