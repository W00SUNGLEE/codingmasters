import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())

people_list = [0 for _ in range(n+1)]
people_list[1] = 1

relation_dict = defaultdict(list)

kim_friend = list()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    relation_dict[a].append(b)
    relation_dict[b].append(a)

for friend in relation_dict[1]:
    people_list[friend] = 1
    kim_friend.append(friend)


for person in kim_friend:
    for friend in relation_dict[person]:
        if people_list[friend] == 0:
            people_list[friend] = 1

print(sum(people_list)-1)