import sys

v, e = map(int, sys.stdin.readline().split())

if v == 1:
    print(0)

else:

    graph = list()

    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().split())

        graph.append([c, a, b])

    graph.sort()

    check_list = [2 for i in range(v+1)]
    check_list[0] = 0

    check_list[graph[0][1]] -= 1
    check_list[graph[0][2]] -= 1

    answer = graph[0][0]

    for i in range(len(graph)):
        if check_list[graph[i][1]] + check_list[graph[i][2]] == 3:
            answer += graph[i][0]
            check_list[graph[i][1]] -= 1
            check_list[graph[i][2]] -= 1

        if sum(check_list) == 2:
            break

    print(answer)