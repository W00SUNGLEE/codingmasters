import random
import time

boomerang_shape = [[[0, 0], [1, 0], [0, 1]],
                   [[0, 1], [0, 0], [1, 1]],
                   [[1, 1], [0, 1], [1, 0]],
                   [[1, 0], [1, 1], [0, 0]]]

answer_list = list()

answer = [0]
tmp = [0]

def find_boomerang(i, j, shape_list):
    if visited[i+ shape_list[0][0]][j+shape_list[0][1]] == 0 and visited[i+shape_list[1][0]][j + shape_list[1][1]] == 0 and visited[i + shape_list[2][0]][j + shape_list[2][1]] == 0:
        tmp[0] += matrix[i + shape_list[0][0]][j + shape_list[0][1]] * 2 + matrix[i + shape_list[1][0]][j + shape_list[1][1]] + matrix[i + shape_list[2][0]][j + shape_list[2][1]]
        visited[i + shape_list[0][0]][j + shape_list[0][1]] = 1
        visited[i + shape_list[1][0]][j + shape_list[1][1]] = 1
        visited[i + shape_list[2][0]][j + shape_list[2][1]] = 1
        dfs(i, j)
        visited[i + shape_list[0][0]][j + shape_list[0][1]] = 0
        visited[i + shape_list[1][0]][j + shape_list[1][1]] = 0
        visited[i + shape_list[2][0]][j + shape_list[2][1]] = 0
        tmp[0] -= matrix[i + shape_list[0][0]][j + shape_list[0][1]] * 2 + matrix[i + shape_list[1][0]][j + shape_list[1][1]] + matrix[i + shape_list[2][0]][j + shape_list[2][1]]

def dfs(a, b):
    for j in range(b, m-1):
        for shape_list in boomerang_shape:
            if 0 <= a + 1 < n and 0 <= j + 1 < m:
                find_boomerang(a, j, shape_list)

    for i in range(a+1, n-1):
        for j in range(m-1):
            for shape_list in boomerang_shape:
                if 0 <= i + 1 < n and 0 <= j + 1 < m:
                    find_boomerang(i, j, shape_list)

    if tmp[0] > answer[0]:
        answer[0] = tmp[0]


def calcIdx(x, y):
    return x * M + y

# idx: 현재 (행 ,열) 위치의 인덱스, sum: 지금까지 만든 부메랑들의 강도의 합
def solve(idx, sum):
    if idx == N * M:  # 마지막에 도달했을 때
        global res
        res = max(res, sum)  # 최댓값을 갱신하고 탐색 종료
        return

    if check[idx]:  # 이미 부메랑을 만드는 데 사용된 칸일 경우에는 탐색 종료
        return

    # 현재 idx에 대한 행과 열
    x = idx // M
    y = idx % M

    # 현재 idx를 기준으로 오른쪽(east), 왼쪽(west), 아래쪽(south), 위쪽(north)에 대한 idx
    eastIdx = calcIdx(x, y+1)
    westIdx = calcIdx(x, y-1)
    southIdx = calcIdx(x+1, y)
    northIdx = calcIdx(x-1, y)

    # ㅁㅁ
    # ㅁ   형태의 부메랑을 만들 수 있는지 확인
    if (x+1 < N and not check[southIdx]) and (y+1 < M and not check[eastIdx]):
        # 만들 수 있을 경우 해당 칸들을 사용했음을 체크하고
        # 현재 idx 이후부터 마지막 idx까지 반복적으로 호출
        check[idx] = True
        check[southIdx] = True
        check[eastIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x+1][y] + board[x][y+1]))
        check[southIdx] = False
        check[eastIdx] = False
        check[idx] = False

    # ㅁㅁ
    #  ㅁ  형태의 부메랑을 만들 수 있는지 확인
    if (y-1 >= 0 and not check[westIdx]) and (x+1 < N and not check[southIdx]):
        check[idx] = True
        check[westIdx] = True
        check[southIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x][y-1] + board[x+1][y]))
        check[westIdx] = False
        check[southIdx] = False
        check[idx] = False

    #   ㅁ
    # ㅁㅁ 형태의 부메랑을 만들 수 있는지 확인
    if (y-1 >= 0 and not check[westIdx]) and (x-1 >= 0 and not check[northIdx]):
        check[idx] = True
        check[westIdx] = True
        check[northIdx] = True
        for i in range(idx+1, N*M+1):
            solve(i, sum + (board[x][y]*2 + board[x][y-1] + board[x-1][y]))
        check[westIdx] = False
        check[northIdx] = False
        check[idx] = False

    # ㅁ
    # ㅁㅁ 형태의 부메랑을 만들 수 있는지 확인
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
    while True:
        n = random.randrange(1, 6)
        m = random.randrange(1, 6)

        visited = [[0 for _ in range(m)] for _ in range(n)]

        answer[0] = 0
        print(n, m)

        matrix = [[] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                matrix[i].append(random.randrange(1, 101))
                print(matrix[i][j], end=" ")

            print()

        N = n
        M = m
        check = [False for _ in range(N*M)]
        res = 0

        board = matrix

        for i in range(N*M):
            solve(i, 0)

        dfs(0, 0)

        print(answer[0])

        print(res)

        if answer[0] != res:
            break