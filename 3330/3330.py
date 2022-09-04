import sys
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())

card = list(map(int, sys.stdin.readline().split()))

answer = [0]
tmp_answer = [0]

def dfs(index, turn):
    if index == -1:
        if tmp_answer[0] > answer[0]:
            answer[0] = tmp_answer[0]
        return None
    else:
        tmp_answer[0] += card[index] * turn
        dfs(index-1, -turn)

        if index-1 > -1:
            tmp_answer[0] += card[index-1] * turn
            dfs(index - 2, -turn)

            if index-2 > -1:
                tmp_answer[0] += card[index - 2] * turn
                dfs(index - 3, -turn)
                tmp_answer[0] -= card[index - 2] * turn

            tmp_answer[0] -= card[index - 1] * turn

        tmp_answer[0] -= card[index] * turn

dfs(n-1, 1)
print(answer[0])