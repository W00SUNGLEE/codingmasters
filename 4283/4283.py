import sys
from collections import deque

n = int(sys.stdin.readline())

game_list = list(map(int, sys.stdin.readline().split()))

game_list.sort(reverse=True)

answer_list = deque()
i = 0

while game_list:
    if i % 2 == 0:
        answer_list.append(game_list.pop())

    else:
        answer_list.appendleft(game_list.pop())

    i += 1

answer = abs(answer_list[0] - answer_list[-1])

for i in range(n-1):
    answer = max(abs(answer_list[i+1] - answer_list[i]), answer)

print(answer)