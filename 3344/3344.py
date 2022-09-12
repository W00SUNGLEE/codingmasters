import sys

string = list(sys.stdin.readline())
sub_string = list(sys.stdin.readline())

index = 0

for i in range(len(string)):
    if string[i] == sub_string[index]:
        index += 1

if index == len(sub_string):
    print("YES")
else:
    print("NO")