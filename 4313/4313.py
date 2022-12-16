import sys
from collections import deque
n = int(sys.stdin.readline())

army_list = [0]
tmp_list = list(map(int, sys.stdin.readline().split()))

army_list.extend(tmp_list)

deq = deque()

answer = 0

check = False

army_list[1] = 0

for i in range(1, n+1):
    if army_list[i] == 1:
        deq.append(i)
        army_list[i] = 0
        check = True

if check:
    answer += 1

while deq:
    check = False

    for _ in range(len(deq)):
        tmp_index = deq.popleft()
        for i in range(1, n + 1):
            if army_list[i] == tmp_index:
                deq.append(i)
                army_list[i] = 0
                check = True

    if check:
        answer += 1

print(answer)