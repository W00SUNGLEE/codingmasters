import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

stack = list()

for i in range(2*n):
    if len(stack) == 0:
        stack.append(arr[i])

    else:
        if arr[i] == stack[len(stack)-1]:
            stack.pop()

        else:
            stack.append(arr[i])

if len(stack) == 0:
    print("YES")

else:
    print("NO")