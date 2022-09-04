import sys

matrix = list()

for _ in range(3):
    matrix.append(list(sys.stdin.readline().strip()))

if matrix[1][1] == "0":
    print("possible")

else:
    print("impossible")#