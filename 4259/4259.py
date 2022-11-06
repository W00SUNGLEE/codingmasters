import sys

move = [(-1, 1), (0, 1), (1, 1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))



answer = 0

for i in range(n):
    index = [i, 0]
    tmp = list()

    for j in range(m-1):
        check = False

        for xi, yi in move:
            new_x = index[0] + xi
            new_y = index[1] + yi
            if 0 <= new_x < n and 0 <= new_y < m:
                if matrix[new_x][new_y] == 'O':
                    matrix[new_x][new_y] = 'X'
                    index[0] = new_x
                    index[1] = new_y
                    tmp.append([new_x, new_y])
                    print(tmp)
                    check = True
                    break

        if check == False:
            for x, y in tmp:
                matrix[x][y] = 'O'
            break

    if index[1] == m-1:
        answer += 1

for a in matrix:
    print(a)

print(answer)