import sys
from itertools import combinations

n = int(sys.stdin.readline())

prim = [1 for _ in range(5000)]

prim[0] = 0
prim[1] = 0

for i in range(2, 5000):
    if prim[i] == 1:
        for j in range(i*2, 5000, i):
            prim[j] = 0

prim_list = list()
for i in range(5000):
    if prim[i] == 1:
        prim_list.append(i)

comb_list = list(combinations(prim_list, 2))

answer = 0
for i in range(len(comb_list)):
    if comb_list[i][0] * comb_list[i][1] <= n:
        answer += 1

print(answer)