import sys
from collections import deque

n = int(sys.stdin.readline())

card_list = deque(list())

card_list.append(0)

for i in range(1, n+1):
    up_down = sys.stdin.readline().strip()

    if up_down == "U":
        card_list.append(i)

    else:
        card_list.appendleft(i)

for card in card_list:
    print(card, end=" ")

print()