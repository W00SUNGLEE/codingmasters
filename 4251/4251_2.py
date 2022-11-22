# 문제가 이상해요 ㅠ_ㅠ
import sys

num = int(sys.stdin.readline())

class ball:
     def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d

balls = []
for i in range(num):
    a,b,c = sys.stdin.readline().split()
    balls.append(ball(int(a),int(b),c))

dx = {"N":-1, "S":1, "W":0,"E":0}
dy = {"N":0, "S":0, "W":-1,"E":1}

ans = 0

for bi in range(len(balls)):
    for bj in range(bi + 1, len(balls)):
        if dx[balls[bi].d] == 0:
            id = (balls[bj].y - balls[bi].y) * dy[balls[bi].d]
        else:
            id = (balls[bj].x - balls[bi].x) * dx[balls[bi].d]
        if dx[balls[bj].d] == 0:
            jd = (balls[bi].y - balls[bj].y) * dy[balls[bj].d]
        else:
            jd = (balls[bi].x - balls[bj].x) * dx[balls[bj].d]

        if id > 0 and id == jd:
           ans += 1

print(ans)