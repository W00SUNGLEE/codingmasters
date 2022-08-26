import sys

H, W = map(int, sys.stdin.readline().split())

img = list()

for _ in range(H):
    img.append(list(sys.stdin.readline().strip()))

h, w = map(int, sys.stdin.readline().split())

avata = list()

for _ in range(h):
    avata.append(list(sys.stdin.readline().strip()))

for i in range(-1, -(h+1), -1):

    for j in range(-1, -(w+1), -1):
        if avata[i][j] != '.':
            img[i][j] = avata[i][j]

for a in img:
    print("".join(a))