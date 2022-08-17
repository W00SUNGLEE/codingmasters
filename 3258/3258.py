import sys

n = int(sys.stdin.readline())

answer = [0, 0]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a == 1:
        if b == 2:
            answer[1] += 1

        elif b == 3:
            answer[0] += 1

    elif a == 2:
        if b == 1:
            answer[0] += 1

        elif b == 3:
            answer[1] += 1

    else: # a == 3:
        if b == 1:
            answer[1] += 1

        elif b == 2:
            answer[0] += 1

print(answer[0], answer[1])