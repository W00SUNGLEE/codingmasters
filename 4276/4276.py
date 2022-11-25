import sys

n = int(sys.stdin.readline())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

one_list = list()
two_list = list()

answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            one_list.append([i, j])

        elif matrix[i][j] == 2:
            two_list.append([i, j])

for two in two_list:
    tmp = 0

    for one in one_list:
        tmp += abs(two[0]-one[0]) + abs(two[1]-one[1])

    answer = min(tmp, answer)

print(answer)

