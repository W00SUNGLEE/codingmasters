import sys
import copy

n = int(sys.stdin.readline())

cube = [[[0+4*i, 1+4*i], [2+4*i, 3+4*i]] for i in range(6)]

for i in range(n):
    tmp_cube = copy.deepcopy(cube)

    command = sys.stdin.readline().strip()

    if command == "U":
        tmp_cube[0][0][0] = cube[0][1][0]
        tmp_cube[0][0][1] = cube[0][0][0]
        tmp_cube[0][1][0] = cube[0][1][1]
        tmp_cube[0][1][1] = cube[0][0][1]

        tmp_cube[1][0][0] = cube[2][0][0]
        tmp_cube[1][0][1] = cube[2][0][1]

        tmp_cube[2][0][0] = cube[4][0][0]
        tmp_cube[2][0][1] = cube[4][0][1]

        tmp_cube[4][0][0] = cube[5][0][0]
        tmp_cube[4][0][1] = cube[5][0][1]

        tmp_cube[5][0][0] = cube[1][0][0]
        tmp_cube[5][0][1] = cube[1][0][1]

    elif command == "U0":
        tmp_cube[0][0][0] = cube[0][0][1]
        tmp_cube[0][0][1] = cube[0][1][1]
        tmp_cube[0][1][0] = cube[0][0][0]
        tmp_cube[0][1][1] = cube[0][1][0]

        tmp_cube[1][0][0] = cube[5][0][0]
        tmp_cube[1][0][1] = cube[5][0][1]

        tmp_cube[2][0][0] = cube[1][0][0]
        tmp_cube[2][0][1] = cube[1][0][1]

        tmp_cube[4][0][0] = cube[2][0][0]
        tmp_cube[4][0][1] = cube[2][0][1]

        tmp_cube[5][0][0] = cube[4][0][0]
        tmp_cube[5][0][1] = cube[4][0][1]

    elif command == "L":
        tmp_cube[5][0][0] = cube[5][1][0]
        tmp_cube[5][0][1] = cube[5][0][0]
        tmp_cube[5][1][0] = cube[5][1][1]
        tmp_cube[5][1][1] = cube[5][0][1]

        tmp_cube[0][0][0] = cube[4][1][1]
        tmp_cube[0][1][0] = cube[4][0][1]

        tmp_cube[1][0][0] = cube[0][0][0]
        tmp_cube[1][1][0] = cube[0][1][0]

        tmp_cube[3][0][0] = cube[1][0][0]
        tmp_cube[3][1][0] = cube[1][1][0]

        tmp_cube[4][0][1] = cube[3][1][0]
        tmp_cube[4][1][1] = cube[3][0][0]

    elif command == "L0":
        tmp_cube[5][0][0] = cube[5][0][1]
        tmp_cube[5][0][1] = cube[5][1][1]
        tmp_cube[5][1][0] = cube[5][0][0]
        tmp_cube[5][1][1] = cube[5][1][0]

        tmp_cube[0][0][0] = cube[1][0][0]
        tmp_cube[0][1][0] = cube[1][1][0]

        tmp_cube[1][0][0] = cube[3][0][0]
        tmp_cube[1][1][0] = cube[3][1][0]

        tmp_cube[3][0][0] = cube[4][1][1]
        tmp_cube[3][1][0] = cube[4][0][1]

        tmp_cube[4][0][1] = cube[0][1][0]
        tmp_cube[4][1][1] = cube[0][0][0]

    elif command == "F":
        tmp_cube[1][0][0] = cube[1][1][0]
        tmp_cube[1][0][1] = cube[1][0][0]
        tmp_cube[1][1][0] = cube[1][1][1]
        tmp_cube[1][1][1] = cube[1][0][1]

        tmp_cube[0][1][0] = cube[5][1][1]
        tmp_cube[0][1][1] = cube[5][0][1]

        tmp_cube[2][0][0] = cube[0][1][0]
        tmp_cube[2][1][0] = cube[0][1][1]

        tmp_cube[3][0][0] = cube[2][1][0]
        tmp_cube[3][0][1] = cube[2][0][0]

        tmp_cube[5][0][1] = cube[3][0][0]
        tmp_cube[5][1][1] = cube[3][0][1]

    elif command == "F0":
        tmp_cube[1][0][0] = cube[1][0][1]
        tmp_cube[1][0][1] = cube[1][1][1]
        tmp_cube[1][1][0] = cube[1][0][0]
        tmp_cube[1][1][1] = cube[1][1][0]

        tmp_cube[0][1][0] = cube[2][0][0]
        tmp_cube[0][1][1] = cube[2][1][0]

        tmp_cube[2][0][0] = cube[3][0][1]
        tmp_cube[2][1][0] = cube[3][0][0]

        tmp_cube[3][0][0] = cube[5][0][1]
        tmp_cube[3][0][1] = cube[5][1][1]

        tmp_cube[5][0][1] = cube[0][1][1]
        tmp_cube[5][1][1] = cube[0][1][0]

    cube = copy.deepcopy(tmp_cube)

cube_list = list()

for i in range(6):
    for j in range(2):
        for k in range(2):
            cube_list.append(cube[i][j][k])

cube_move_dict = dict()

for i in range(len(cube_list)):
    cube_move_dict[cube_list[i]] = i

#answer_cube = [i//4 for i in range(24)]
moving_cube = [i//4 for i in range(24)]

answer = 0

tmp_cube = list()

for i in range(len(moving_cube)):
    tmp_cube.append(moving_cube[cube_move_dict[i]])

moving_cube = copy.deepcopy(tmp_cube)

answer += 1

def check_cube(cube):
    check = True

    for i in range(6):
        for j in range(4):
            if cube[4*i+j] != cube[4*i]:
                check = False
                break

    return check

while check_cube(moving_cube) == False:
    tmp_cube = list()

    for i in range(len(moving_cube)):
        tmp_cube.append(moving_cube[cube_move_dict[i]])

    moving_cube = copy.deepcopy(tmp_cube)

    answer += 1

print(answer)