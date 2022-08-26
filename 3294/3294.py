import sys

n = int(sys.stdin.readline())

tmp = 0

stat = [0, 0, 0, 0]

for i in range(n):
    game = sys.stdin.readline().strip()

    if game == "WIN":
        if stat[1] == 0:
            stat[0] += 1
        else:
            stat[1] = 0
            stat[0] += 1

    else:
        if stat[0] == 0:
            stat[1] += 1
        else:
            stat[0] = 0
            stat[1] += 1

    if stat[1] > stat[3]:
        stat[3] = stat[1]

    if stat[0] > stat[2]:
        stat[2] = stat[0]

    print(stat[0], stat[1], stat[2], stat[3])