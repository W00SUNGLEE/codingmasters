import sys

n = int(sys.stdin.readline())

dic = dict()

for _ in range(n):
    key, value = sys.stdin.readline().split()

    dic[key] = value

find = sys.stdin.readline().strip()

if find in dic.keys():
    print(dic[find])
else:
    print(-1)