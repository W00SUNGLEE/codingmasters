import sys

n = int(sys.stdin.readline())

pen_list = list(map(int, sys.stdin.readline().split()))

pen_list.sort(reverse=True)

answer = max(pen_list[0] * pen_list[1] * pen_list[2], pen_list[0] * pen_list[1], pen_list[-1] * pen_list[-2] * pen_list[0], pen_list[-1] * pen_list[-2])

print(answer)