arr = list()

n, r = map(int, input().split())

for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp not in arr:
        arr.append(tmp)

answer = [-100, -100]
count = 0

for i in range(-100, 101):
    for j in range(-100, 101):
        tmp_count = 0
        for k in range(len(arr)):
            x = arr[k][0]
            y = arr[k][1]
            if (x - i)*(x - i) + (y - j)*(y - j) <= r*r:
                tmp_count += 1

        if tmp_count > count:
            answer[0] = i
            answer[1] = j
            count = tmp_count

print("{} {}".format(round(answer[0]), round(answer[1])))