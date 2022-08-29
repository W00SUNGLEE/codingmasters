import sys
from collections import defaultdict

n = int(sys.stdin.readline())

if n == 1:
    print(n)

else:
    counter_answer = defaultdict(int)
    counter_answer[1] += 1

    answer = []

    for _ in range(3, n+1):
        tmp_dic = defaultdict(int)

        for key in counter_answer.keys():
            tmp_dic[key] += 1

        for value in counter_answer.values():
            tmp_dic[value] += 1
        counter_answer = tmp_dic.copy()

    for key, value in counter_answer.items():
        answer.append(key)
        answer.append(value)

    answer = "".join(map(str, answer))
    print(answer)


