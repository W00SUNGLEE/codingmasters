import sys

n = int(sys.stdin.readline())

energy_list = list()

for _ in range(4):
    energy_list.append(list(map(int, sys.stdin.readline().split())))

def energy(index, count, state):
    visited[index] = 0
    tmp_answer[0] += energy_list[state][index]
    dfs(count + 1)
    tmp_answer[0] -= energy_list[state][index]
    visited[index] = 1

def dfs(count):
    if count == n:
        answer[0] = min(tmp_answer[0], answer[0])

    if tmp_answer[0] > answer[0]:
        return None

    tmp = 0

    for i in range(n):
        if visited[i] == 1:
            tmp += min(energy_list[0][i], energy_list[1][i], energy_list[2][i], energy_list[3][i])

    if tmp_answer[0] + tmp > answer[0]:
        return None

    for i in range(n):
        if visited[i] == 1:
            if i == 0:
                if visited[i+1] == 1:
                    energy(i, count, 2)

                else:
                    energy(i, count, 3)

            elif i == n-1:
                if visited[i-1] == 1:
                    energy(i, count, 1)

                else:
                    energy(i, count, 3)

            else:
                if visited[i-1] == 1 and visited[i+1] == 1:
                    energy(i, count, 0)
                elif visited[i-1] == 1 and visited[i+1] != 1:
                    energy(i, count, 1)
                elif visited[i-1] != 1 and visited[i+1] == 1:
                    energy(i, count, 2)
                else:
                    energy(i, count, 3)

if n == 1:
    print(energy_list[3][0])

else:

    visited = [1 for _ in range(n)]

    answer = [sys.maxsize]
    tmp_answer = [0]

    dfs(0)

    print(answer[0])