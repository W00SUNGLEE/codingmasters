import sys

move = [(-1, 1), (0, 1), (1, 1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

answer = [0]
def dfs(x, y):

    if y == m-1:
        answer[0] += 1
        return True

    else:

        for xi, yi in move:
            new_x = x + xi
            new_y = y + yi
            if 0 <= new_x < n and 0 <= new_y < m:
                if matrix[new_x][new_y] == 'O':
                    matrix[new_x][new_y] = 'X'
                    check = dfs(new_x, new_y)

                    if check:
                        return True

                    else:
                        matrix[new_x][new_y] = 'O'


        return False

for i in range(n):
    dfs(i, 0)

print(answer[0])