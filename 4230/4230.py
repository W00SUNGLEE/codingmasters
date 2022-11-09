import sys

n, m = map(int, sys.stdin.readline().split())

weapon_list = list(map(int, sys.stdin.readline().split()))


tmp_list = list(map(int, sys.stdin.readline().split()))
weakness_list = [0 for _ in range(10001)]

max_weakness = max(tmp_list)

for weakness in tmp_list:
    weakness_list[weakness] = 1

weapon_list.sort()

answer = "NO"

for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if weapon_list[i] + weapon_list[j] + weapon_list[k] > max_weakness:
                break

            if weakness_list[weapon_list[i] + weapon_list[j] + weapon_list[k]] == 1:
                answer = "YES"
                break

        if answer == "YES":
            break

    if answer == "YES":
        break

print(answer)