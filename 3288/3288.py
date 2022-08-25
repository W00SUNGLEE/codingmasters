import sys
from collections import defaultdict

n = int(sys.stdin.readline())

sticks = list(map(int, sys.stdin.readline().split()))

sticks_dic = defaultdict(int)

answer_stick = list()
answer_stick2 = list()

for i in range(len(sticks)):
    sticks_dic[sticks[i]] += 1

for key, value in sticks_dic.items():
    if value > 1:
        answer_stick.append(key)
    if value > 3:
        answer_stick2.append(key)

answer_stick.sort()
answer_stick2.sort()

answer = 0
answer2 = 0

if len(answer_stick) > 1:
    answer = answer_stick[-1] * answer_stick[-2]
if len(answer_stick2) > 0:
    answer2 = answer_stick2[-1] ** 2

print(max(answer, answer2))
