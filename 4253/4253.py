import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

mine_list = list(map(int, sys.stdin.readline().split()))

value = (k+1)//2

value_list = deque()
value_list.append(value)

for i in range(value-1, 0, -1):
    value_list.append(i)
    value_list.appendleft(i)


answer = -sys.maxsize
answer_list = list()

for i in range(n-k+1):
    tmp_answer = 0
    for j in range(k):
        tmp_answer += mine_list[i+j]*value_list[j]

    answer_list.append(tmp_answer)
    answer = max(tmp_answer, answer)

print(answer)