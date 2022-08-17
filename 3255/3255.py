import sys

n, m = map(int, sys.stdin.readline().split())

arr = []

def mix(a, b):
    if a == "R":
        if b == "R":
            return "R"
        elif b == "G":
            return "Y"
        else: # b =="B"
            return "M"
    elif a == "G":
        if b == "R":
            return "Y"
        elif b == "G":
            return "G"
        else: # b =="B"
            return "C"
    else: # a == "B":
        if b == "R":
            return "M"
        elif b == "G":
            return "C"
        else: # b =="B"
            return "B"

for i in range(n):
    arr.append(list(sys.stdin.readline().split()))

for i in range(n):
    tmp = list(sys.stdin.readline().split())
    for j in range(m):
        print(mix(arr[i][j], tmp[j]), end=" ")

    print()