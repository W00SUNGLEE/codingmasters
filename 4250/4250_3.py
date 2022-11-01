import sys
from collections import defaultdict
text = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

word_list = list()

for i in range(n):
    tmp = sys.stdin.readline().strip()
    word_list.append([-len(tmp), tmp])

index = 0

word_list.sort()

while index < len(text):
    tmp_list = list()
    tmp_dic = defaultdict(list)

    for word in word_list:
        find_index = text.find(word[1], index)

        if find_index >= 0:
            tmp_dic[len(word[1])].append(find_index)
        else:
            continue

    if len(tmp_dic.keys()) == 0:
        break

    else:
        key = list(tmp_dic.keys())[0]
        tmp_dic[key].sort()
        index = tmp_dic[key][0] + key

    print(index)



    break