import sys

n = int(sys.stdin.readline())

line_list = list()

for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    line_list.append([[a, b], [c, d]])
    line_list[i].sort()

def ccw(p1, p2, p3):
    ccw_result = (p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1]);

    if ccw_result > 0:
        return 1

    elif ccw_result < 0:
        return -1

    else:
        return 0

def comparator(left, right):
    if left[0] == right[0]:
        result = (left[1] <= right[1]);

    else:
        result = (left[0] <= right[0])

    return result

def intersect(line1, line2):
    ccw_1_2 = ccw(line1[0], line1[1], line2[0]) * ccw(line1[0], line1[1], line2[1])
    ccw_2_1 = ccw(line2[0], line2[1], line1[0]) * ccw(line2[0], line2[1], line1[1])

    if ccw_1_2 == 0 and ccw_2_1 == 0:
        result = comparator(line2[0], line1[1]) and comparator(line1[0], line2[1])

    else:
        result = ccw_1_2 <= 0 and ccw_2_1 <= 0

    if result:
        return 1
    else:
        return 0

answer = 0

for i in range(n):
    for j in range(i+1, n):
        answer += intersect(line_list[i], line_list[j])

print(answer)