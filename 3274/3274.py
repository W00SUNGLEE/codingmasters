import sys

n = int(sys.stdin.readline())

if n % 2 == 0:
    print("jjajangmyeon")

else:
    if n % 4 == 1:
        print("jjamppong")

    else:
        print("bokkeumbap")