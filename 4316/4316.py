import sys

n = int(sys.stdin.readline())

meal_list = list()

for i in range(n):
    year, name = sys.stdin.readline().split()

    meal_list.append([-int(year), i, name])

meal_list.sort()

for i in range(n):
    print(meal_list[i][2])