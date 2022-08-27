import sys

time_list = list(map(int, sys.stdin.readline().split(":")))

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())

day = 24*60*60

time= time_list[0]*60*60+time_list[1]*60+time_list[2]

time += t*(n-1)

if time > day:
    time -= day

second = time % 60
time = time // 60
minutes = time % 60
hour = time // 60

print("{:0>2}:{:0>2}:{:0>2}".format(hour, minutes, second))