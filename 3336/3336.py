import sys
import heapq
import copy

line = list(sys.stdin.readline().strip())

n = len(line)

blank_index = [0, 0]

queue = list()

switch = [(1, 0), (-1, 0), (0, 1), (0, -1)]

save = list()

answer = -1

for i in range(n):
    if line[i] == "X":
        line[i] = "0"
        blank_index[0] = 0
        blank_index[1] = i

matrix = list()
matrix.append(list(map(int, line)))

for i in range(1, n):
    line = list(sys.stdin.readline().strip())

    for j in range(n):
        if line[j] == "X":
            line[j] = "0"
            blank_index[0] = i
            blank_index[1] = j

    matrix.append(list(map(int, line)))

answer_matrix = [[0 for _ in range(n)] for _ in range(n)]

count = 1

for i in range(n):
    for j in range(n):
        answer_matrix[i][j] = count
        count += 1
        if answer_matrix[i][j] == n * n:
            answer_matrix[i][j] = 0

def check_h(matrix, n):
    h = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != answer_matrix[i][j]:
                h += 1

    return h

print(check_h(matrix, n))
g = 0
h = check_h(matrix, n)
f = g + h

heapq.heappush(queue, [f, g, h, matrix, blank_index])

while queue:
    f, g, h, matrix, blank_index = heapq.heappop(queue)

    print("f : {}, g : {}, h : {}, blank_index : {}".format(f, g, h, blank_index))
    for a in matrix:
        print(a)

    if h == 0:
        answer = f
        break

    if matrix in save:
        continue

    else:
        save.append(matrix)

        for x, y in switch:
            xi = blank_index[0] + x
            yi = blank_index[1] + y

            if 0 <= xi < n and 0 <= yi < n:
                matrix[blank_index[0]][blank_index[1]] = matrix[xi][yi]
                matrix[xi][yi] = 0

                new_g = g + 1
                new_h = check_h(matrix, n)
                new_f = new_g + new_h

                heapq.heappush(queue, [new_f, new_g, new_h, copy.deepcopy(matrix), [xi, yi]])

                matrix[xi][yi] = matrix[blank_index[0]][blank_index[1]]
                matrix[blank_index[0]][blank_index[1]] = 0

print(answer)