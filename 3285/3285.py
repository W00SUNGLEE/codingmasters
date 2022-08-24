import sys

n = int(sys.stdin.readline())

x, y = map(int, sys.stdin.readline().split())

answer = sys.maxsize

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    tmp_answer = (abs(x-a) + abs(y-b))*100

    if tmp_answer < answer:
        answer = tmp_answer

print(answer)