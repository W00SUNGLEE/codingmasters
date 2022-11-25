import sys

n, m = map(int, sys.stdin.readline().split())

matrix = list()

for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

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

answer = 0

for i in range(n):
    for j in range(m):
        for tetromino in tetrominos:
            x = len(tetromino)
            y = len(tetromino[0])

            if i+x-1 < n and j+y-1 < m:
                tmp = 0
                for a in range(x):
                    for b in range(y):
                        if tetromino[a][b] == "#":
                            tmp += matrix[i+a][j+b]

                answer = max(tmp, answer)

print(answer)