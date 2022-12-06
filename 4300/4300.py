import sys

a, b = map(int, sys.stdin.readline().split())

n, m = map(int, sys.stdin.readline().split())

option_list = list()

for _ in range(n):
    option_list.append(int(sys.stdin.readline()))

option_list.sort(reverse=True)

option_price = 0

for i in range(m):
    option_price += option_list[i]

answer = a + (b * option_price)

print(answer)