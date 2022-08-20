import sys

a, b = map(int, sys.stdin.readline().split())

if a > b :
    print(min(a-b, 60-(a-b)))

else:
    print(min(b-a, 60-(b-a)))