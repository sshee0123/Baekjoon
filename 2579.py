import sys
n = int(sys.stdin.readline())
d = [0] * 301
s = [0] * 301
for i in range(n):
    s[i] = int(sys.stdin.readline())
    d[0] = s[0]
    d[1] = s[0] + s[1]
    d[2] = max(s[1]+s[2], s[0]+s[2])
    for i in range(3,n):
        d[i] = max(d[i-3]+s[i-1]+s[i], d[i-2]+s[i])
print(d[n-1])