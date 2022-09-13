import sys

n = int(sys.stdin.readline())

time = 12*60*60

time -= n

second = time % 60
time = time // 60
minutes = time % 60
hour = time // 60

print("{:0>2}:{:0>2}:{:0>2}".format(hour, minutes, second))