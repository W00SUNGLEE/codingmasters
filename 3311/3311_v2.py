import sys
import math

length = 10
half_length = length // 2
n, r = map(int, sys.stdin.readline().split())

matrix = [[0 for _ in range(length+1)] for _ in range(length+1)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x += half_length
    y += half_length

    for i in range(x-r, x+r+1):
        for j in range(y-r, y+r+1):
            if 0 <= i <= length and 0 <= j <= length:
                if math.sqrt((x-i)*(x-i) + (y-j)*(y-j)) <= r:
                    matrix[i][j] += 1

    for a in matrix:
        print(a)

    print()

answer = [0, 0]
max_count = -1

for i in range(length):
    for j in range(length):
        if matrix[i][j] > max_count:
            max_count = matrix[i][j]
            answer[0] = i-half_length
            answer[1] = j-half_length

print("{} {}".format(answer[0], answer[1]))

