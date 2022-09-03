import sys

n, m, k = map(int, sys.stdin.readline().split())

weight = [0]

for _ in range(n):
    weight.append(int(sys.stdin.readline()))

check = [0 for _ in range(n+1)]

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())

    matrix[a][b] = 1
    matrix[b][a] = 1

answer = 0

for _ in range(n):
    max_weight = 0
    index = 0
    for i in range(1, n+1):
        if check[i] == 0 and weight[i] > max_weight:
            max_weight = weight[i]
            index = i

    check[index] = 1

    for i in range(1, n+1):
        if check[i] == 0 and matrix[index][i] == 1:
            if weight[index] - weight[i] > k:
                answer += weight[index] - weight[i] - k
                weight[i] = weight[index] - k
            else:
                continue

print(answer)