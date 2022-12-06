import sys
from copy import deepcopy
from collections import defaultdict

n = int(sys.stdin.readline())

score_list = list(map(int, sys.stdin.readline().split()))

tmp_list = deepcopy(score_list)

tmp_list.sort(reverse=True)

rank_dic = defaultdict(int)

rank = 1

for i in range(n):
    if rank_dic[tmp_list[i]] > 0:
        continue

    else:
        rank_dic[tmp_list[i]] = i+1

for i in range(n):
    print(score_list[i], rank_dic[score_list[i]])