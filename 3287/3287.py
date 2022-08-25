import sys

n = int(sys.stdin.readline())

shopping_list = list()

for i in range(1, n+1):
    tmp = list(map(int, sys.stdin.readline().split()))

    tmp.append(i)
    tmp[0] = -tmp[0]
    shopping_list.append(tmp)

shopping_list.sort()

for i in range(len(shopping_list)):
    print(shopping_list[i][3], end=" ")

print()