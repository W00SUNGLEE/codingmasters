import sys

n = int(sys.stdin.readline())

answer = [[1]]

for i in range(1, n):
    tmp = [[0 for _ in range(i+1)] for _ in range(i+1)]
    for x in range(i):
        for y in range(i):

            tmp[x][y] += answer[x][y]
            tmp[x+1][y] += answer[x][y]
            tmp[x][y+1] += answer[x][y]

    answer.clear()
    answer = tmp

for i in range(len(answer)):
    for j in range(len(answer)-i):
        print(answer[i][j], end=" ")
    print()