import sys
from collections import deque

string = sys.stdin.readline().strip()

for i in range(len(string)):
    if "0" <= string[i] <= "9":
        column = string[:i]
        row = string[i:]
        break

column = column

column_list = deque([i for i in column])

for i in range(len(column)-1, -1, -1):
    if ord(column[i]) - 1 == 64:
        if i == 0 :
            column_list.popleft()
            break
        else:
            column_list[i] = "Z"

    else:
        column_list[i] = chr(ord(column[i]) -1)
        break


print("".join(column_list), row, sep="")
print(column, int(row)-1, sep="")