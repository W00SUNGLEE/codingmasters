import sys

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

boomerang_list = list()


for i in range(n-1):
    for j in range(m-1):
        boomerang_list.append([matrix[i][j]*2 + matrix[i][j + 1] + matrix[i + 1][j], [[i, j], [i, j+1], [i+1, j]]])
        boomerang_list.append([matrix[i][j+1]*2 + matrix[i][j] + matrix[i + 1][j + 1], [[i, j+1], [i, j], [i + 1, j + 1]]])
        boomerang_list.append([matrix[i + 1][j + 1]*2 + matrix[i][j + 1] + matrix[i + 1][j], [[i + 1, j + 1], [i, j + 1], [i + 1, j]]])
        boomerang_list.append([matrix[i + 1][j]*2 + matrix[i][j] + matrix[i + 1][j + 1], [[i + 1, j], [i, j], [i + 1, j + 1]]])

boomerang_list.sort(reverse=True)

answer = 0

for i in range(len(boomerang_list)-1):
    for j in range(len(boomerang_list)):
        if boomerang_list[i][0] + boomerang_list[j][0] < answer:
            break

        else:
            check = True
            for k in range(3):
                if boomerang_list[i][1][k] in boomerang_list[j][1]:
                    check = False
                    break

            if check:
                answer = boomerang_list[i][0] + boomerang_list[j][0]

print(answer)