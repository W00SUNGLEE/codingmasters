import sys

n, k = map(int, sys.stdin.readline().split())

stock_list = list(map(int, sys.stdin.readline().split()))

decrese_list = list()
decrese_list.append(0)
for i in range(n-1):
    if stock_list[i] > stock_list[i+1]:
        decrese_list.append(i+1)

decrese_list.append(n+1)

length = 0

answer = [0, 0]

if len(decrese_list)-k-1 <= 0:
    print(1, n)

else:
    for i in range(len(decrese_list)-k-1):
        if decrese_list[i+k+1] - decrese_list[i] - 1 >= length:
            length = decrese_list[i+k+1] - decrese_list[i] - 1
            answer[0] = decrese_list[i]+1
            answer[1] = decrese_list[i+k+1] -1

    print(answer[0], answer[1])