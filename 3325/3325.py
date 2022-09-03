import sys

min_string = list(sys.stdin.readline().strip())
max_string = min_string.copy()

min_count = 0
max_count = 0

for i in range(len(min_string)):
    if min_string[i] == "x":
        if i == 0:
            min_string[i] = "o"
            max_string[i] = "g"

        else:
            if min_string[i-1] == "o":
                min_string[i] = "o"

            else:
                min_string[i] = "g"

            if max_string[i - 1] == "o":
                max_string[i] = "g"

            else:
                max_string[i] = "o"

min_ground = 0
max_ground = 0

for i in range(len(min_string)):
    if min_string[i] == "g":
        min_ground = 1
    else:
        if min_ground == 1:
            min_count += 1
        min_ground = 0

    if max_string[i] == "g":
        max_ground = 1
    else:
        if max_ground == 1:
            max_count += 1
        max_ground = 0

print(min_count)
print(max_count)
