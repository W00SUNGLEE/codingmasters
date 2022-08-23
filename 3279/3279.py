import sys

string = sys.stdin.readline()

if "." in string:
    print("IPv4")

else:
    print("IPv6")