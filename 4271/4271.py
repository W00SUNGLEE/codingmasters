import sys

n = int(sys.stdin.readline())

monkey_list = list(map(int, sys.stdin.readline().split()))

total = int(sys.stdin.readline())

sum_monkey = sum(monkey_list)

if sum_monkey <= total:
    monkey_list.sort(reverse=True)
    print(monkey_list[0])

else:
    tmp_list = [0 for _ in range(n)]

    for i in range(10000000000):
        for j in range(n):
            if tmp_list[j] + 1 <= monkey_list[j]:
                tmp_list[j] += 1

        sum_tmp = sum(tmp_list)
        if sum_tmp > total:
            print(i)
            break