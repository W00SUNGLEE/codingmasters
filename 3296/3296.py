import sys
from collections import defaultdict
import math

length = int(sys.stdin.readline())
n = int(sys.stdin.readline())

data = defaultdict()

answer = list()

hour = 60 * 60

for _ in range(n*2):
    input_list = list(sys.stdin.readline().split())

    time_list = list(map(int, input_list[1].split(":")))
    time = time_list[0] * 60 * 60 + time_list[1] * 60 + time_list[2]
    if input_list[0] not in data.keys():
        data[input_list[0]] = time

    elif input_list[0] in data.keys():
        speed = length / ((time - data[input_list[0]]) / hour)

        answer.append([input_list[0], speed])

answer.sort()

for number, speed in answer:
    print(number, math.floor(speed))
