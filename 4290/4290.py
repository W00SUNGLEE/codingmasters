import sys
from itertools import combinations

n = int(sys.stdin.readline())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

number_list = [i for i in range(n)]

combinations_list = list(combinations(number_list, n // 2))

answer = sys.maxsize

for first_list in combinations_list:
    second_list = list()

    for i in range(n):
        if i not in first_list:
            second_list.append(i)

    first_score = 0
    second_score = 0

    for i in range(n//2):
        for j in range(i+1, n//2):
            first_score += matrix[first_list[i]][first_list[j]] + matrix[first_list[j]][first_list[i]]
            second_score += matrix[second_list[i]][second_list[j]] + matrix[second_list[j]][second_list[i]]


    answer = min(abs(first_score-second_score), answer)

print(answer)