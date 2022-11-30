import sys

n, m = map(int, sys.stdin.readline().split())

mother_list = [0 for _ in range(n+1)]
child_list = [0 for _ in range(n+1)]

tmp_list = list()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    mother_list[a] += 1
    child_list[b] += 1

    tmp_list.append([a, b])

sort_list = list()

for i in range(m):
    sort_list.append([child_list[tmp_list[i][1]], mother_list[tmp_list[i][0]], tmp_list[i][0], tmp_list[i][1]])

sort_list.sort(reverse=True)

answer_list = [0 for _ in range(n+1)]

answer = list()


# print(mother_list)
# print(child_list)
# print(sort_list)

while sort_list:
    tmp = sort_list.pop()

    if mother_list[tmp[2]] > 0 and answer_list[tmp[3]] == 0:
        #mother_list[tmp[2]] = 0
        answer_list[tmp[3]] = 1

        answer.append([tmp[2], tmp[3]])

print(sum(answer_list))

