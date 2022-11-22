import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())

tmp_dic = defaultdict(int)

for _ in range(n):
    tmp_dic[sys.stdin.readline().strip()] += 1

deq = deque()

for key, value in tmp_dic.items():
    x, y, direction = key.split()
    deq.append([2 * int(x), 2 * int(y), direction, value])

answer = 0

while deq:
    tmp_dic = defaultdict(list)
    for _ in range(len(deq)):
        x, y, direction, count = deq.popleft()

        if direction == "N":
            x -= 1
        elif direction == "S":
            x += 1
        elif direction == "W":
            y -= 1
        elif direction == "E":
            y += 1

        if 0 <= x <= 2000 and 0 <= y <= 2000:
            tmp_dic[10000*x + y].append(count)

            deq.append([x, y, direction, count])

    for value in tmp_dic.values():
        if len(value) > 1:
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    answer += value[i] * value[j]

print(answer)