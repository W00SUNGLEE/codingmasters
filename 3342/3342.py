import sys
from collections import deque

string1 = deque(list(sys.stdin.readline().strip()))
string2 = deque(list(sys.stdin.readline().strip()))

answer = "NO"

for i in range(len(string1)):
    string1.appendleft(string1.pop())

    tmp = True
    for j in range(len(string1)):
        if string1[j] != string2[j]:
            tmp = False
            break

    if tmp:
        answer = "YES"
        break

print(answer)