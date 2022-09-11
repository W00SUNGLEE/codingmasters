import sys

n, k = map(int, sys.stdin.readline().split())

score = list(map(int, sys.stdin.readline().split()))
sort_score = score.copy()
sort_score.sort()

answer = 999999999
check = -1

for i in sort_score:
    check_score = [0 for _ in range(n)]
    tmp_check = 0

    for j in range(n):
        if score[j] >= i:
            check_score[j] = 1

            if j-1 >= 0:
                check_score[j-1] = 1

            if j+1 < n:
                check_score[j+1] = 1

    tmp_check = sum(check_score)

    if check < tmp_check <= k:
        answer = i
        check = tmp_check

    elif check == tmp_check and tmp_check <= k:
        if i > answer:
            answer = i
        check = tmp_check

print(answer)