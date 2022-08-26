import sys

answer = list()

button_list = list(map(int, sys.stdin.readline().split()))

if button_list[0] == 1:
    answer.append("L")
elif button_list[0] == 2:
    answer.append("L")
else:
    answer.append("R")

for i in range(1, len(button_list)):
    if button_list[i] == 1:
        answer.append("L")
    elif button_list[i] == 2:
        if answer[-1] == "L":
            answer.append("R")
        else:
            answer.append("L")
    else:
        answer.append("R")

for i in range(len(answer)):
    print(answer[i], end=" ")

print()