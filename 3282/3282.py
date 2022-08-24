import sys

n, m = map(int, sys.stdin.readline().split())

move = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

answer = 0

for i in range(n):
    for j in range(m):
        tmp_answer = 0

        for x, y in move:
            xi = x + i
            yi = y + j

            if 0 <= xi < n and 0 <= yi < m:
                tmp_answer += matrix[xi][yi]

        if tmp_answer > answer:
            answer = tmp_answer

print(answer)