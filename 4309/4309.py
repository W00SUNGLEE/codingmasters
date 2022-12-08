import sys

n = int(sys.stdin.readline())

enemy_list = list()

for i in range(n):
    enemy_list.append(int(sys.stdin.readline()))

b, c = map(int, sys.stdin.readline().split())

answer = 0

for i in range(n):

    if enemy_list[i] - b <= 0:
        answer += 1

    else:
        if (enemy_list[i]-b) % c != 0:
            answer += 1 + ((enemy_list[i]-b)//c+1)

        else:
            answer += 1 + (enemy_list[i] - b) // c

print(answer)