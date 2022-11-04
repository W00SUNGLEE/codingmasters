import sys
import bisect

def A(f,a):
    q = bisect.bisect_left(f,a)

    if q:
        if len(f)!=q:
            f[q]=a
        else:
            f.append(a)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = 0

for i in range(len(a)):
    c,d=[a[i]],[-a[i]]
    for t in range(i, len(a)):
        A(c,a[t])
        A(d,-a[t])
    m=max(m,len(c)+len(d)-1)

print(m)