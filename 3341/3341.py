import sys

input_string = list(sys.stdin.readline().strip())
target_string = list(sys.stdin.readline().strip())

input_arr = list()
target_arr = list()

def parsing(string, arr):
    index = 0
    while index < len(string):
        tmp = string[index]
        count = 1
        index += 1

        while index < len(string) and string[index] == tmp:
            index += 1
            count += 1

        arr.append(count)

parsing(input_string, input_arr)
parsing(target_string, target_arr)

answer = 0

while sum(input_arr) != sum(target_arr):
    for i in range(len(input_arr)):
        if input_arr[i] < target_arr[i]:
            for j in range(input_arr[i], 0, -1):
                if input_arr[i] + j <= target_arr[i]:
                    input_arr[i] += j
                    break
            i += 1
            check = True
            while check and i < len(input_arr) and input_arr[i] < target_arr[i]:
                for j in range(input_arr[i], 0, -1):
                    if input_arr[i]+j <= target_arr[i]:
                        if j < input_arr[i]:
                            check = False
                        input_arr[i] += j
                        break
                i += 1
            answer += 1
            break

print(answer)