import sys

string = sys.stdin.readline().strip()

answer = list()

for i in range(len(string)):

    for j in range(i+1, len(string)+1):
        if len(string) % (j-i) == 0:
            tmp = string[i:j]
            if string == tmp * (len(string) // (j-i)):
                answer.append(tmp)

answer.sort()
print(answer[0])