import sys

text = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

word_list = list()

for i in range(n):
    word_list.append(sys.stdin.readline().strip())

index = 0

word_list.sort(reverse=True)

answer = 0

while index < len(text):

    tmp_list = [[0, 0] for _ in range(len(word_list))]
    for i in range(index, len(text)):
        for j in range(len(word_list)):
            if i + len(word_list[j]) - 1 >= len(text):
                continue

            else:
                if text[i:i + len(word_list[j])] == word_list[j] and tmp_list[j][0] == 0:
                    tmp_list[j][0] = -len(word_list[j])
                    tmp_list[j][1] = i + len(word_list[j])
                    break

        plus += len(word_list[i]) - 1