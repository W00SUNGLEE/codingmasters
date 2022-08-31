import sys

arr = list(map(int, sys.stdin.readline().strip()))

answer = "NO"

if arr[0]+arr[1] == arr[2]+arr[3]:
    answer = "YES"

elif arr[0]+arr[2] == arr[1]+arr[3]:
    answer = "YES"

elif arr[0]+arr[3] == arr[1]+arr[2]:
    answer = "YES"

print(answer)