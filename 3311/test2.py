arr = list()

n, r = map(int, input().split())

for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp not in arr:
        arr.append(tmp)

matrix = [[0 for _ in range(21)] for _ in range(21)]
answer = [-10, -10]
count = 0

for i in range(-10, 11):
    for j in range(-10, 11):
        tmp_count = 0
        for k in range(len(arr)):
            x = arr[k][0]
            y = arr[k][1]
            if (x - i)*(x - i) + (y - j)*(y - j) <= r*r:
                tmp_count += 1
                matrix[i+10][j+10] += 1

        if tmp_count > count:
            answer[0] = i
            answer[1] = j
            count = tmp_count

print("{} {}".format(round(answer[0]), round(answer[1])))
for a in matrix:
    print(a)