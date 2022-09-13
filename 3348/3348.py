import sys

n = int(sys.stdin.readline())

rectangle = list()
rectangle.append(list())

for _ in range(n):
    rectangle.append(list(map(int, sys.stdin.readline().split())))

intersection_space = -1
answer = [0, 0]

for i in range(1, n+1):

    for j in range(i+1, n+1):
        tmp_intersection_space = 0

        intersect_X = min(rectangle[i][0]+rectangle[i][2], rectangle[j][0]+rectangle[j][2]) - max(rectangle[i][0], rectangle[j][0])
        intersect_Y = min(rectangle[i][1]+rectangle[i][3], rectangle[j][1]+rectangle[j][3]) - max(rectangle[i][1], rectangle[j][1])

        if intersect_X <= 0 or intersect_Y <= 0:
            tmp_intersection_space = 0

        else:
            tmp_intersection_space = intersect_X * intersect_Y / (rectangle[i][2]*rectangle[i][3] + rectangle[j][2]*rectangle[j][3] - intersect_X * intersect_Y)

        if tmp_intersection_space > intersection_space:
            intersection_space = tmp_intersection_space
            answer = [i, j]

print(answer[0], answer[1])