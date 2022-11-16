import sys

n = int(sys.stdin.readline())

work_list = list()

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    check = False

    for i in range(len(work_list)-1, -1 , -1):
        if (a < work_list[i][1] and b < work_list[i][0]) or (a > work_list[i][1] and b > work_list[i][0]):
            continue
        else:
            a = min(a, work_list[i][0])
            b = max(b, work_list[i][1])
            work_list.pop(i)

    work_list.append([a, b])

answer = 100000

for i in range(len(work_list)):
    answer -= work_list[i][1] - work_list[i][0] + 1

print(answer)