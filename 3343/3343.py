import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

matrix = list()
count = 0
answer = [0]

for _ in range(n):
    input_string = list(sys.stdin.readline().strip())
    tmp = list()

    for i in range(n):
        if input_string[i] == '.':
            tmp.append(1)
            count += 1
        else:
            tmp.append(0)

    matrix.append(tmp)

def dfs(count):
    if count == 0:
        answer[0] += 1
        return None

    check = False

    for i in range(n):
        if check:
            break
        for j in range(n):
            if check:
                break
            if matrix[i][j] == 1:
                if i+1 < n and matrix[i+1][j] == 1:
                    matrix[i][j] = 0
                    matrix[i + 1][j] = 0
                    dfs(count-2)
                    matrix[i][j] = 1
                    matrix[i + 1][j] = 1
                    check = True

                if j+1 < n and matrix[i][j+1] == 1:
                    matrix[i][j] = 0
                    matrix[i][j + 1] = 0
                    dfs(count-2)
                    matrix[i][j] = 1
                    matrix[i][j + 1] = 1
                    check = True


dfs(count)
print(answer[0])