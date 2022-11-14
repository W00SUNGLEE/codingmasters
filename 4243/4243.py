import sys

n, m, x = map(int, sys.stdin.readline().split())

person_list = list(map(int, sys.stdin.readline().split()))

m = len(person_list)

if n >= m:
    print(m)

else:
    ride_list = list()

    answer_list = list()

    for i in range(n):
        if len(person_list) > 0:
            ride_list.append(person_list.pop(0))

    while len(ride_list) > 0:
        min_ride_list = min(ride_list)

        for _ in range(min_ride_list):
            answer_list.append(len(ride_list))

        for i in range(len(ride_list)-1, -1, -1):
            ride_list[i] -= min_ride_list
            if ride_list[i] == 0:
                ride_list.pop(i)

        for i in range(n-len(ride_list)):
            if len(person_list) > 0:
                ride_list.append(person_list.pop(0))

    print(answer_list[(x-1) % len(answer_list)])