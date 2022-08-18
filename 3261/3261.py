import sys

java = float(sys.stdin.readline().replace("s", ""))
python = float(sys.stdin.readline().replace("s", ""))

if java > python:
    print("PYTHON")

else:
    print("JAVA")