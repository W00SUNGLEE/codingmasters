import sys

n, m = map(int, sys.stdin.readline().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, list(sys.stdin.readline().strip()))))

answer = 0

for i in range(n):
    for j in range(m):

        for a in range(1, n+1):
            if i+a > n:
                break

            for b in range(1, m+1):
                if j+b > m:
                    break

                tmp_answer = 0

                for x in range(i, i+a):
                    tmp_answer += sum(matrix[x][j:j+b])

                if tmp_answer == a*b:
                    answer += 1

print(answer)