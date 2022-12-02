# import sys
# from collections import defaultdict
# import math
#
# n = int(sys.stdin.readline())
#
# answer_list = [0 for _ in range(n)]
# answer_link = defaultdict(list)
#
# a, b, c, d = map(int, sys.stdin.readline().split())
#
# answer_list[a] = c
# answer_list[b] = d
#
#
# for _ in range(n-2):
#     a, b, c, d = map(int, sys.stdin.readline().split())
#
#     if answer_list[a] == 0 and answer_list[b] == 0:
#         answer_list[a] = c
#         answer_list[b] = d
#
#     elif answer_list[a] != 0 and answer_list[b] == 0:
#         if c == answer_list[a]:
#             answer_list[b] = d
#
#         else:
#             lcm = math.lcm(c, answer_list[a])
#
#             for a_link in answer_link[a]:
#                 answer_list[a_link] = answer_list[a_link]
#
#             answer_list[b] = d * (lcm // c)
#
#     elif answer_list[a] == 0 and answer_list[b] != 0:
#
#     else:
#
#     answer_link[a].append(b)
#     answer_link[b].append(a)



#math.lcm()