n = int(input())

if n < 4:
    print(0)
else:
    i = 4
    tmp = 0
    answer = 0
    while i != n+1:
        if i % 4 == 0:
            tmp += 1
            answer = tmp**2
        elif i % 4 == 2:
            answer += tmp

        print(answer)
        i += 1

print(answer)
