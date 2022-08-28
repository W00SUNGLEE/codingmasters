import sys

string = list(sys.stdin.readline().split())

year = int(string[0])

if string[3] == "Private":
    if year == 0:
        print(0)
    elif 1 <= year <= 4:
        if string[2] == "N":
            if string[1] == "ROKAF":
                print(28)
            else:
                print(32)
        else:
            print(28)
    else:
        print(20)
else:
    if year == 0:
        print(0)
    else:
        print(28)