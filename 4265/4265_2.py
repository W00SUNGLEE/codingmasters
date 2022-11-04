import sys

n, m = map(int, sys.stdin.readline().split())

matrix = list()

sum_row = list()

for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    sum_row.append(sum(matrix[i]))

sum_total = sum(sum_row)

if n % 2 == 1:
    print(sum_total)

else:
    answer = 0

    for i in range(n-1):
        if i % 2 == 0:
            for j in range(m):
                tmp = sum_total - sum_row[i] - sum_row[i + 1]
                tmp += sum(matrix[i][:j+1]) + sum(matrix[i+1][j:])
                answer = max(tmp, answer)

        else:
            for j in range(m):
                tmp = sum_total - sum_row[i] - sum_row[i + 1]
                tmp += sum(matrix[i][j:]) + sum(matrix[i+1][:j+1])
                answer = max(tmp, answer)

    print(answer)





