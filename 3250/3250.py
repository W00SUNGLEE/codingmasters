import sys

dic1 = {"MON": 0, "TUE" : 1, "WED" : 2, "THU": 3, "FRI": 4, "SAT" : 5, "SUN" : 6}

dic2 = {0 : "MON",1 : "TUE", 2 : "WED", 3 : "THU", 4 : "FRI", 5 : "SAT", 6 : "SUN"}

n = int(sys.stdin.readline())

tmp = sys.stdin.readline().strip()

print( dic2[(n + dic1[tmp]) % 7])