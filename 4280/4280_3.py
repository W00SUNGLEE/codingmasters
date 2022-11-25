def calcIdx(x, y):
    return x * M + y

def solve(idx, sum):
    if idx == N * M:
        global res
        res = max(res, sum)
        return

    if check[idx]:
        return

    x = idx // M
    y = idx % M

    eastIdx = calcIdx(x, y+1)
    westIdx = calcIdx(x, y-1)
    southIdx = calcIdx(x+1, y)
    northIdx = calcIdx(x-1, y)

    if (x+1 < N and not check[southIdx]) and (y+1 < M and not check[eastIdx]):
        check[idx] = True
        check[southIdx] = True
        check[eastIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x+1][y] + board[x][y+1]))
        check[southIdx] = False
        check[eastIdx] = False
        check[idx] = False

    if (y-1 >= 0 and not check[westIdx]) and (x+1 < N and not check[southIdx]):
        check[idx] = True
        check[westIdx] = True
        check[southIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x][y-1] + board[x+1][y]))
        check[westIdx] = False
        check[southIdx] = False
        check[idx] = False

    if (y-1 >= 0 and not check[westIdx]) and (x-1 >= 0 and not check[northIdx]):
        check[idx] = True
        check[westIdx] = True
        check[northIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x][y-1] + board[x-1][y]))
        check[westIdx] = False
        check[northIdx] = False
        check[idx] = False

    if (x-1 >= 0 and not check[northIdx]) and (y+1 < M and not check[eastIdx]):
        check[idx] = True
        check[northIdx] = True
        check[eastIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x-1][y] + board[x][y+1]))
        check[northIdx] = False
        check[eastIdx] = False
        check[idx] = False

if __name__ == '__main__':
    N, M = map(int, input().split())
    board = []
    check = [False for _ in range(N*M)]
    res = 0

    for _ in range(N):
        board.append(list(map(int, input().split())))

    for i in range(N*M):
        solve(i, 0)

    print(res)