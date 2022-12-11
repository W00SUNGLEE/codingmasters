import sys

n, m = map(int, sys.stdin.readline().split())

baggage_list = list()
bag_size_list = list()

for i in range(n):
    size, price = map(int, sys.stdin.readline().split())
    baggage_list.append([-price, size, 1])

for i in range(m):
    bag_size_list.append(int(sys.stdin.readline()))

baggage_list.sort()
bag_size_list.sort()

answer = 0

for i in range(len(bag_size_list)):
    for j in range(len(baggage_list)):
        if baggage_list[j][1] <= bag_size_list[i] and baggage_list[j][2] == 1:
            answer += -baggage_list[j][0]
            baggage_list[j][2] = 0
            break

print(answer)