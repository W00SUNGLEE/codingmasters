import sys

n = int(sys.stdin.readline())

student_list = list()

for i in range(n):
    name, score = sys.stdin.readline().split()

    student_list.append([int(score), name])

student_list.sort(reverse=True)

for i in range(n):
    print(student_list[i][1], end=" ")