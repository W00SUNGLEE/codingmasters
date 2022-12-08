import sys

n, m = map(int, sys.stdin.readline().split())

refund_list = list()

for i in range(n):
    refund_list.append(int(sys.stdin.readline()))

refund_list.sort(reverse=True)

price = 0
answer = 0

for i in range(n):
    if price + refund_list[i] > m:
        continue

    else:
        price += refund_list[i]
        answer += 1

print(answer)