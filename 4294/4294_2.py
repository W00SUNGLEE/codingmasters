import sys
from collections import deque
import math

n = int(sys.stdin.readline())

info_dic = dict()

link_list = list()

visited = [0 for _ in range(n)]

deq = deque()

for _ in range(n-1):
    a, b, c, d = map(int, sys.stdin.readline().split())
    gcd = math.gcd(c, d)

    if gcd > 1:
        c //= gcd
        d //= gcd

    info_dic[(a, b)] = [c, d]
    info_dic[(b, a)] = [d, c]

    link_list.append([a, b])
    link_list.append([b, a])

print(link_list)
print(info_dic)

answer_list = [0 for _ in range(n)]

deq.append(0)
visited[0] = 1

def lcm_func(x, y):
    return (x * y) // math.gcd(x, y)

while deq:
    index = deq.popleft()

    for a, b in link_list:
        if index == a:
            if answer_list[index] == 0:
                c, d = info_dic[(a, b)]
                answer_list[a] = c
                answer_list[b] = d

            else:
                c, d = info_dic[(a, b)]
                lcm = lcm_func(c, answer_list[index])
                tmp = lcm // answer_list[index]

                for i in range(len(answer_list)):
                    answer_list[i] = answer_list[i] * tmp

                if answer_list[b] == 0:
                    answer_list[b] = d * (lcm // c)

            if visited[b] == 0:
                visited[b] = 1
                deq.append(b)

gcd = math.gcd(*answer_list)

for i in range(len(answer_list)):
    print(answer_list[i]//gcd, end=" ")