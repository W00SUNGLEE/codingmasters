# -*- coding: utf-8 -*-
import sys

dishes = list(map(int, sys.stdin.readline().split()))
prices = [1000, 1500, 2000, 3000, 5000]

answer = 0

for i in range(5):
    answer += dishes[i] * prices[i]

print(answer)