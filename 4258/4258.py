import sys
from collections import defaultdict, deque

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(sys.stdin.readline().strip()))

answer_list = [0, 0]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "A" or matrix[i][j] == "B":
            color_dic = defaultdict(int)
            color_dic["A"] = 0
            color_dic["B"] = 0
            color_dic[matrix[i][j]] += 1

            deq = deque()

            deq.append((i, j))
            matrix[i][j] = "X"

            while deq:
                x, y = deq.pop()

                for xi, yi in move:
                    new_x = x + xi
                    new_y = y + yi

                    if 0 <= new_x < n and 0 <= new_y < m:
                        if matrix[new_x][new_y] == "A" or matrix[new_x][new_y] == "B":
                            color_dic[matrix[new_x][new_y]] += 1
                            matrix[new_x][new_y] = "X"
                            deq.append((new_x, new_y))

                        if matrix[new_x][new_y] == "O":
                            matrix[new_x][new_y] = "X"
                            deq.append((new_x, new_y))


            if color_dic["A"] > color_dic["B"]:
                answer_list[0] += color_dic["A"]

            else:
                answer_list[1] += color_dic["B"]

print(answer_list[0], answer_list[1])