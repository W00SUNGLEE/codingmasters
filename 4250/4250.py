import sys

text = sys.stdin.readline().strip()

n = int(sys.stdin.readline())

word_list = list()

for i in range(n):
    word_list.append(sys.stdin.readline().strip())

index = 0

word_list.sort(reverse=True)
#print(word_list)

answer = 0
answer_list = []

while index < len(text):

    plus = 0

    for i in range(len(word_list)):
        if index + len(word_list[i]) - 1 >= len(text):
            continue

        else:
            if text[index:index + len(word_list[i])] == word_list[i]:
                plus += len(word_list[i])
                answer += 1
                answer_list.append(word_list[i])
                break

    index += plus + 1

print(answer)