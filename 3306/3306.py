import sys

n = int(sys.stdin.readline().strip())

prim = [i for i in range(n+1)]

prim[0] = 0
prim[1] = 0

for i in range(2, n+1):
    if prim[i] == 0:
        continue

    else:
        for j in range(i*2, n+1, i):
            prim[j] = 0

if prim[n] == n:
    print("clap")

else:
    print(n)