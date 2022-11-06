import sys
import copy

n = int(sys.stdin.readline())

fighter_list = list()
max_fight_score = 0

for i in range(n):
    name, fight_score = sys.stdin.readline().split()
    fighter_list.append((name, int(fight_score)))
    max_fight_score = max(fighter_list[i][1], max_fight_score)

answer_list = list()

while len(fighter_list) > 1:
    tmp = list()

    for i in range(0, len(fighter_list), 2):
        if fighter_list[i][1] > fighter_list[i+1][1]:
            tmp.append(fighter_list[i])
            if fighter_list[i][1] == max_fight_score:
                answer_list.append(fighter_list[i+1][0])

        else:
            tmp.append(fighter_list[i+1])
            if fighter_list[i+1][1] == max_fight_score:
                answer_list.append(fighter_list[i][0])

    fighter_list = copy.deepcopy(tmp)

for i in range(len(answer_list)):
    print(answer_list[i])