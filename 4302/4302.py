import sys

n = int(sys.stdin.readline())

weight_list = list(map(int, sys.stdin.readline().split()))

start, end = map(int, sys.stdin.readline().split())

print(min(weight_list[start-1:end]))