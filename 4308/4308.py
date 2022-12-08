import sys
import math

n = int(sys.stdin.readline())

if n == 1:
    print(0)

else:
    answer = 1

    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            answer = 0
            break

    print(answer)

