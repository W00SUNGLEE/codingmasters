import sys

string = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

for _ in range(n):
    s, t, cur = sys.stdin.readline().split()

    cur = int(cur)

    string = string[0:cur] + string[cur:].replace(s, t, 1)
    print(string)