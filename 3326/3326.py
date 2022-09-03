import sys
import copy
from itertools import permutations

n1, m1 = map(int, sys.stdin.readline().split())

permutation = [i for i in range(1, n1+1)]
permutation_list = list(permutations(permutation))

grape1 = list()

for _ in range(m1):
    u, v = map(int, sys.stdin.readline().split())
    tmp = [u, v]
    tmp.sort()
    grape1.append(tmp)

grape1.sort()

n, m = map(int, sys.stdin.readline().split())

grape2 = list()

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    tmp = [u, v]
    tmp.sort()
    grape2.append(tmp)

if n1 != n or m1 != m:
    print("NO")
    exit()

tmp_grape = list()
answer = "NO"

for permutation in permutation_list:
    del tmp_grape
    tmp_grape = copy.deepcopy(grape2)

    for i in range(m):
        for j in range(2):
            tmp_grape[i][j] = permutation[tmp_grape[i][j]-1]

        tmp_grape[i].sort()
    tmp_grape.sort()

    check = True

    for i in range(m):
        for j in range(2):
            if grape1[i][j] != tmp_grape[i][j]:
                check = False
                break

        if not check:
            break

    if check:
        answer = "YES"
        break

print(answer)
