import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

N = 2*n

matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]

check = [0 for _ in range(N+1)]

answer = [-sys.maxsize]
tmp_answer = [0]

for _ in range(k):
    a, b, c = map(int, sys.stdin.readline().split())

    matrix[b][c] = a
    matrix[c][b] = a

def dfs(N):
    if sum(check) == N:
        if tmp_answer[0] > answer[0]:
            answer[0] = tmp_answer[0]
        return None

    else:
        for i in range(1, N+1):
            if check[i] == 1:
                continue

            else:
                for j in range(i+1, N+1):
                    if check[j] == 1:
                        continue

                    else:
                        if matrix[i][j] == 1:
                            tmp_answer[0] += 1
                        elif matrix[i][j] == 2:
                            tmp_answer[0] -= 1

                        check[i] += 1
                        check[j] += 1
                        dfs(N)
                        check[i] -= 1
                        check[j] -= 1

                        if matrix[i][j] == 1:
                            tmp_answer[0] -= 1
                        elif matrix[i][j] == 2:
                            tmp_answer[0] += 1

dfs(N)
print(answer[0])