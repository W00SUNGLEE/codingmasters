import sys

n = int(sys.stdin.readline())

apartment = list()

for i in range(n):
    apartment.append(list(map(int, sys.stdin.readline().split())))

length_sum = sys.maxsize

answer = 0

for i in range(len(apartment)):
    tmp = 0

    for j, people in apartment:
        tmp += abs(apartment[i][0]-j) * people

    if tmp < length_sum:
        length_sum = tmp
        answer = i+1

print(answer)