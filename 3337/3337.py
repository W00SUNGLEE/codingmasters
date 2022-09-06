import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

answer = "NO"

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            for l in range(k+1, n):
                if arr[i] * arr[j] == arr[k] * arr[l]:
                    answer = "YES"

                if arr[i] * arr[k] == arr[j] * arr[l]:
                    answer = "YES"

                if arr[i] * arr[l] == arr[j] * arr[k]:
                    answer = "YES"

print(answer)