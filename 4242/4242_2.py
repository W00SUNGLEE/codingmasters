import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

energy_list = list()

for _ in range(4):
    energy_list.append(list(map(int, sys.stdin.readline().split())))

dp = [sys.maxsize for _ in range(1 << n)]
dp[0] = 0

answer = [sys.maxsize]

tmp_answer = [0]

def energy(visited, index, state):
    if tmp_answer[0] + energy_list[state][index] < dp[visited | (1 << index)]:
        dp[visited | (1 << index)] = tmp_answer[0]+energy_list[state][index]
        tmp_answer[0] += energy_list[state][index]
        dfs(visited | (1 << index))
        tmp_answer[0] -= energy_list[state][index]

def dfs(visited):
    if visited == (1 << n) - 1:
        answer[0] = min(tmp_answer[0], answer[0])
        return None

    if tmp_answer[0] > dp[visited]:
        return None

    for i in range(n):
        if visited & (1 << i):
            continue

        else:
            if i == 0:
                if not(visited & (1 << (i + 1))):
                    energy(visited, i, 2)

                else:
                    energy(visited, i, 3)

            elif i == n - 1:
                if not(visited & (1 << (i - 1))):
                    energy(visited, i, 1)

                else:
                    energy(visited, i, 3)

            else:
                if not(visited & (1 << (i - 1))) and not(visited & (1 << (i + 1))):
                    energy(visited, i, 0)
                elif not(visited & (1 << (i - 1))) and visited & (1 << (i + 1)):
                    energy(visited, i, 1)
                elif visited & (1 << (i - 1)) and not(visited & (1 << (i + 1))):
                    energy(visited, i, 2)
                else:
                    energy(visited, i, 3)

if n == 1:
    print(energy_list[3][0])

else:
    dfs(0)
    print(answer[0])