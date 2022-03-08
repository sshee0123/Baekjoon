#11053
import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
d = [0]*n

for i in range(n):
    for j in range(i):
        if a[j] < a[i] and d[j] > d[i]:
            d[i] = d[j]
    d[i] += 1
print(max(d))