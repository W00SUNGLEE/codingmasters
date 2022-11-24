import sys
import heapq

right_left = [(0, 1), (0, -1)]
up_down = [(-1, 0), (1, 0)]

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

d = int(sys.stdin.readline())

item_list = list()

for _ in range(d):
    a, b = map(int, sys.stdin.readline().split())
    item_list.append((a-1, b-1))

start_x = 0
start_y = 0

answer = matrix[0][0]

for a, b in item_list:
    save_matrix = [[sys.maxsize for _ in range(m)] for _ in range(n)]

    queue = list()

    heapq.heappush(queue, (0, start_x, start_y))
    save_matrix[start_x][start_y] = 0

    while queue:
        damage, x, y = heapq.heappop(queue)

        if damage > save_matrix[x][y]:
            continue

        if x == a and y == b:
            answer += damage
            break

        else:
            for xi, yi in right_left:
                new_x = x + xi
                new_y = y + yi

                if 0 <= new_x < n and 0 <= new_y < m:
                    if damage + matrix[new_x][new_y] < save_matrix[new_x][new_y]:
                        save_matrix[new_x][new_y] = damage + matrix[new_x][new_y]
                        heapq.heappush(queue, (damage + matrix[new_x][new_y], new_x, new_y))

            if y == 0 or y == m-1:
                for xi, yi in up_down:
                    new_x = x + xi
                    new_y = y + yi

                    if 0 <= new_x < n and 0 <= new_y < m:
                        if damage + matrix[new_x][new_y] < save_matrix[new_x][new_y]:
                            save_matrix[new_x][new_y] = damage + matrix[new_x][new_y]
                            heapq.heappush(queue, (damage + matrix[new_x][new_y], new_x, new_y))

    start_x = a
    start_y = b

print(answer)