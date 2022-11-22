import sys
from collections import defaultdict, deque

n, m, k = map(int, sys.stdin.readline().split())

gas_station_dic = defaultdict(lambda: defaultdict(int))

for _ in range(k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a > b:
        continue

    else:
        if c > gas_station_dic[a][b]:
            gas_station_dic[a][b] = c

dp = [0 for _ in range(n+1)]

deq = deque()

deq.append((1, 0))

while deq:
    index, save_mileage = deq.popleft()

    for destination, mileage in gas_station_dic[index].items():
        if index < destination <= n and mileage + save_mileage > dp[destination]:
            dp[destination] = mileage + save_mileage
            deq.append((destination, mileage + save_mileage))

print(dp[-1])