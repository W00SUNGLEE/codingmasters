import sys

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in  range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

cat_painted = False
cat_escaped = False

answer = 0

while True:
    answer += 1

    cat_list = list()
    paint_list = list()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                cat_list.append([i, j])

                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    cat_escaped = True

            if matrix[i][j] == 2:
                paint_list.append([i, j])

    if cat_escaped:
        break

    if len(cat_list) == 0:
        cat_painted = True
        break

    for x, y in cat_list:
        for xi, yi in move:
            new_x = x + xi
            new_y = y + yi

            if 0 <= new_x < n and 0 <= new_y < m:
                if matrix[new_x][new_y] == 0:
                    matrix[new_x][new_y] = 1


    for x, y in paint_list:
        for xi, yi in move:
            new_x = x + xi
            new_y = y + yi

            if 0 <= new_x < n and 0 <= new_y < m:
                if matrix[new_x][new_y] == 0 or matrix[new_x][new_y] == 1:
                    matrix[new_x][new_y] = 2

if cat_painted:
    print("IMPOSSIBLE")

else:
    print(answer)
