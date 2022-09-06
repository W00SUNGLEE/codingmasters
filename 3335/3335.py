import sys

p, q = map(int, sys.stdin.readline().split())

visited = [-1 for _ in range(q)]

save = list()

start = [0, 0]

check = True

while True:
    p *= 10

    if visited[p % q] == p//q:
        start = [p // q, p % q]
        break

    save.append([p // q, p % q])

    visited[p % q] = p//q
    p %= q

print("0.", end="")

for i in range(len(save)):
    if save[i][0] == 0 and save[i][1] == 0:
        break

    if check and save[i][0] == start[0] and save[i][1] == start[1]:
        print("{", end="")
        check = False

    print(save[i][0], end="")

if not check:
    print("}", end="")
print()