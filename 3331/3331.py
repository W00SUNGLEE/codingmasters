import sys

n = int(sys.stdin.readline())

for i in range(3**(n-1)):
    for j in range(3**(n-1)):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            if ((i // 3) % 2 == 0 and (j // 3) % 2 == 0) or ((i // 3) % 2 == 1 and (j // 3) % 2 == 1):
                if ((i // 9) % 2 == 0 and (j // 9) % 2 == 0) or ((i // 9) % 2 == 1 and (j // 9) % 2 == 1):
                    if ((i // 27) % 2 == 0 and (j // 27) % 2 == 0) or ((i // 27) % 2 == 1 and (j // 27) % 2 == 1):
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
            else:
                print(" ", end="")
        else:
            print(" ", end="")
    print()