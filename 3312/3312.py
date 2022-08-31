import sys
from collections import deque

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

queue = deque(list())

queue.append(num_list[0])
queue.append(num_list[1])
queue.append(num_list[2])

answer = sum(queue) - max(queue) - min(queue)

for i in range(3, n):
    queue.popleft()
    queue.append(num_list[i])

    tmp_answer = sum(queue) - max(queue) - min(queue)

    if tmp_answer > answer:
        answer = tmp_answer

print(answer)