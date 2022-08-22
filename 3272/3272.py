import sys

arr = sys.stdin.readline().strip()

clap = False

for i in range(len(arr)):
    if arr[i] == "3":
        print("clap", end="")
        clap = True

    if arr[i] == "6":
        print("clap", end="")
        clap = True

    if arr[i] == "9":
        print("clap", end="")
        clap = True

if not clap:
    print(arr)
else:
    print()