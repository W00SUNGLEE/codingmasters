import sys
import math

n = int(sys.stdin.readline())

print(math.comb(2*n, n)//(n+1)%1000000007)