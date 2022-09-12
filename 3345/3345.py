import sys

matrix = list()

for _ in range(5):
    matrix.append(list(sys.stdin.readline().strip()))

tetrominos = [
    [['#', '#', '#', '#']],
    [['#'],
     ['#'],
     ['#'],
     ['#']],
    [['#', '#'],
     ['#', '#']],
    [['#', '#', '#'],
     ['.', '#', '.']],
    [['.', '#', '.'],
     ['#.', '#', '#']],
    [['.', '#'],
     ['#', '#'],
     ['.', '#']],
    [['#', '.'],
     ['#', '#'],
     ['#', '.']],
    [['#', '#', '#'],
     ['.', '.', '#']],
    [['#', '.', '.'],
     ['#', '#', '#']],
    [['#', '#'],
     ['#', '.'],
     ['#', '.']],
    [['.', '#'],
     ['.', '#'],
     ['#', '#']],
    [['#', '#', '#'],
     ['#', '.', '.']],
    [['.', '.', '#'],
     ['#', '#', '#']],
    [['#', '#'],
     ['.', '#'],
     ['.', '#']],
    [['#', '.'],
     ['#', '.'],
     ['#', '#']],
    [['.', '#', '#'],
     ['#', '#', '.']],
    [['#', '.'],
     ['#', '#'],
     ['.', '#']],
    [['#', '#', '.'],
     ['.', '#', '#']],
    [['.', '#'],
     ['#', '#'],
     ['#', '.']]
]
hash_count = 0
answer = "NO"

for i in range(5):
    for j in range(5):
        if matrix[i][j] == "#":
            hash_count += 1

        for tetromino in tetrominos:
            x = len(tetromino)
            y = len(tetromino[0])

            correct_count = 0
            if i+x-1 < 5 and j+y-1 < 5:
                for a in range(x):
                    for b in range(y):
                        if matrix[i+a][j+b] == tetromino[a][b]:
                            correct_count += 1

            if correct_count == x * y:
                answer = "YES"

if hash_count == 4:
    print(answer)

else:
    print("NO")