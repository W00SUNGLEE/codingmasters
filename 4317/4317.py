import sys
from collections import defaultdict

n = int(sys.stdin.readline())

candidate_dict = defaultdict(int)

for i in range(n):
    candidate_dict[int(sys.stdin.readline())] += 1

answer = 0
max_stock = 0

for key, value in candidate_dict.items():
    if value > max_stock:
        max_stock = value
        answer = key

    elif value == max_stock:
        if key < answer:
            answer = key

print(answer)