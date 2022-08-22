import sys

string = sys.stdin.readline().strip()

for i in range(len(string)):
    if string[i] == "\'":
        print("\\\'", end="")
    elif string[i] == "\"":
        print("\\\"", end="")
    elif string[i] == "\\":
        print("\\\\", end="")
    else:
        print(string[i], end="")