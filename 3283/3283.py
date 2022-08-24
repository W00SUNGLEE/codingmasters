import sys

n = int(sys.stdin.readline())

input_list = list(sys.stdin.readline())

student = list()

answer = 0

for i in range(n):
    if input_list[i] == "O":
        student.append(1)
    else:
        student.append(0)

for i in range(1, n-1):
    if student[i-1] == 1 and student[i+1] == 1:
        student[i - 1] = 0
        student[i + 1] = 0
        answer += 1

answer += sum(student)
print(answer)
