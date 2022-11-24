import sys
import copy

n, start, m = map(int, sys.stdin.readline().split())

dock_list = list(map(int, sys.stdin.readline().split()))

count = [0 for _ in range(n+1)]
count[start] = 1


for i in range(m):
    tmp = [0 for _ in range(n+1)]
    for j in range(1, n+1):
        if count[j] == 1:
            if 1 <= j + dock_list[i] <= n:
                tmp[j + dock_list[i]] = 1

            if 1 <= j - dock_list[i] <= n:
                tmp[j - dock_list[i]] = 1

    count = copy.deepcopy(tmp)

answer = 0

for i in range(n, -1, -1):
    if count[i] == 1:
        answer = i
        break

print(answer)