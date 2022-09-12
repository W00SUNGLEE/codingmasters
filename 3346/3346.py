import sys
from itertools import permutations

string = list(sys.stdin.readline().strip())
n = int("".join(string))

permutations_string = list(permutations(string, len(string)))

answer = "NO"

for permutation_string in permutations_string:
    number = int("".join(permutation_string))

    if int("".join(permutation_string)) % 13 == 0:
        answer = "YES"
        break

print(answer)
