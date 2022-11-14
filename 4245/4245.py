import sys

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

answer = [0]
check = [1, 0]

def dfs():
    if check[0] == n:
        answer[0] += 1
        return None

    if check[0] > n or check[1] > n:
        return None

    if check[0] < check[1]:
        return None

    else:
        check[0] += 1
        dfs()
        check[0] -= 1

        check[1] += 1
        dfs()
        check[1] -= 1

dfs()
print(answer[0] % 1000000007)