import sys

matrix = list()

n = 10

move = [(-1, 0), (0, -1)]

for _ in range(n):
    matrix.append(list(map(int, list(sys.stdin.readline().strip()))))

bug = [-1, -1]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            matrix[i][j] = 0
            bug[0] = i
            bug[1] = j
            break

    if bug != [-1, -1]:
        break

move_state = 0
save = list()

answer = "yes"

while 0 <= bug[0] < n and 0 <= bug[1] < n:
    if [bug[0], bug[1], move_state] in save:
        answer = "no"
        break

    else:
        save.append([bug[0], bug[1], move_state])

        x = bug[0] + move[move_state][0]
        y = bug[1] + move[move_state][1]

        if 0 <= x < n and 0 <= y < n:
            if matrix[x][y] == 0:
                bug[0] = x
                bug[1] = y

            else:
                move_state = (move_state + 1) % 2

        else:
            bug[0] = x
            bug[1] = y

print(answer)