import sys
import math

n = int(sys.stdin.readline())

if n == 1:
    print("IMPOSSIBLE")

else:
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            m = n // i

            check = True
            for j in range(2, int(math.sqrt(m)+1)):
                if m % j == 0:
                    check = False
                    break

            if check:
                print(i, m)
            else:
                print("IMPOSSIBLE")

            break