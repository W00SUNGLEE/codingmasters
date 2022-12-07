import sys
from itertools import product

n = int(sys.stdin.readline())

zero_one = (0, 1)

case_list = list(product(zero_one, repeat=n))

for i in range(len(case_list)):
    for j in range(n):
        print(case_list[i][j], end="")

    print()