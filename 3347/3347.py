import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
snake = list(sys.stdin.readline().strip())
move_commands = list(sys.stdin.readline().strip())

queue = deque(list())
matrix_queue = list()

for i in range(n):
    queue.append([-i, 0])

# 3번째 값: 방향 (상하좌우:0123)
move = [[[-1, 0, 2], [0, 1, 0], [1, 0, 3]],
        [[1, 0, 3], [0, -1, 1], [-1, 0, 2]],
        [[0, -1, 1], [-1, 0, 2], [0, 1, 0]],
        [[0, 1, 0], [1, 0, 3], [0, -1, 1]]]

# 시작좌표 0, 0, 우방향 3
head = [0, 0, 3]

for i in range(m):
    move_command = move_commands[i]

    if move_command == "L":
        head[0] = head[0] + move[head[2]][0][0]
        head[1] = head[1] + move[head[2]][0][1]
        head[2] = move[head[2]][0][2]
    elif move_command == "F":
        head[0] = head[0] + move[head[2]][1][0]
        head[1] = head[1] + move[head[2]][1][1]
        head[2] = move[head[2]][1][2]
    else:
        head[0] = head[0] + move[head[2]][2][0]
        head[1] = head[1] + move[head[2]][2][1]
        head[2] = move[head[2]][2][2]

    queue.appendleft([head[0], head[1]])

for i in range(n):
    x, y = queue.popleft()
    matrix_queue.append([-y, x, snake[i]])

matrix_queue.sort()

for i in range(n):
    print(matrix_queue[i][2], end="")
print()