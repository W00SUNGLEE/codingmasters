# convex hull : https://www.crocus.co.kr/1288
# ccw : https://johoonday.tistory.com/102
import sys
import math

n = int(sys.stdin.readline())

point_list = list()

for _ in range(n):
    point_list.append(list(map(int, sys.stdin.readline().split())))

point_list.sort()
arctan_list = list()

for i in range(1, len(point_list)):

    if point_list[i][1]-point_list[0][1] == 0:
        arctan_list.append([2, i])

    else:
        arctan = math.atan((point_list[i][0]-point_list[0][0]) / (point_list[i][1]-point_list[0][1]))

        if arctan >= 0:
            arctan_list.append([arctan, i])

        else:
            arctan_list.append([4+arctan, i])

arctan_list.sort()

point_sort_list = list()

point_sort_list.append((point_list[0]))

for i in range(len(arctan_list)):
    point_sort_list.append(point_list[arctan_list[i][1]])

def height_width(a, b):
    return [b[0] - a[0], b[1] - a[1]]

def ccw(a, b, c):
    a_b = height_width(a, b)
    b_c = height_width(b, c)

    if a_b[0] * b_c[1] - a_b[1] * b_c[0] < 0:
        return True

    else:
        return False

convex = list()

answer = 0

for c in point_sort_list:
    while len(convex) >= 2:
        a, b = convex[-2], convex[-1]

        if ccw(a, b, c):
            break

        convex.pop()

    convex.append(c)

answer = len(convex)

print(answer)

