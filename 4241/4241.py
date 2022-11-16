import sys
import math
n, m, k, q = map(int, sys.stdin.readline().split())

s = sys.stdin.readline().strip()


matrix = list()

tmp = 0

string_length = len(s)

for _ in range(n):
    tmp_list = list()

    for _ in range(m):
        tmp_list.append(s[tmp])

        if tmp == string_length-1:
            tmp = 0

        else:
            tmp += 1

    matrix.append(tmp_list)

alpha_dic = {'a':[1, 0], 'b':[2, 1], 'c':[3, 1], 'd':[4, 1], 'e':[5, 0],
             'f':[6, 1], 'g':[7, 1], 'h':[8, 1], 'i':[9, 0], 'j':[10, 1],
             'k':[11, 1], 'l':[12, 1], 'm':[13, 1], 'n':[14, 1], 'o':[15, 0],
             'p':[16, 1], 'q':[17, 1], 'r':[18, 1], 's':[19, 1], 't':[20, 1],
             'u':[21, 0], 'v':[22, 1], 'w':[23, 1], 'x':[24, 1], 'y':[25, 1],
             'z':[26, 1]}

log_k = int(math.log2(k)) + 1

dp = [[[[-1, -1]] * log_k for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        x = i
        y = j
        alpha = alpha_dic[matrix[x][y]]

        if alpha[1] == 0:
            distance = alpha[0] % n
            if (x + y) % 2 == 1:
                if x - distance >= 0:
                    x -= distance

                else:
                    x = n + (x - distance)

            else:
                if x + distance < n:
                    x += distance

                else:
                    x = x + distance - n

        if alpha[1] == 1:
            distance = alpha[0] % m
            if (x + y) % 2 == 1:
                if y - distance >= 0:
                    y -= distance

                else:
                    y = m + (y - distance)

            else:
                if y + distance < m:
                    y += distance

                else:
                    y = y + distance - m

        dp[i][j][0][0] = x
        dp[i][j][0][1] = y

for l in range(1, log_k):
    for i in range(n):
        for j in range(m):
            pre_dp = dp[i][j][l-1]
            dp[i][j][l] = dp[pre_dp[0]][pre_dp[1]][l-1]

answer = [0, 0]

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1
    y -= 1
    tmp_x = x
    tmp_y = y
    a = x
    b = y
    for l in range(log_k-1, -1, -1):
        if k & (1 << l):
            a = dp[tmp_x][tmp_y][l][0]
            b = dp[tmp_x][tmp_y][l][1]
            tmp_x = a
            tmp_y = b

    answer[0] += a+1
    answer[1] += b+1

print(answer[0], answer[1])

