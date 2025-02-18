import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
d = [0] * n # 합배열
for i in range(n-1):
    minnum = i
    for j in range(i+1, n):
        if p[minnum] > p[j]:
            minnum = j
    p[minnum], p[i] = p[i], p[minnum]

d[0] = p[0]
for i in range(n-1):
    d[i+1] = d[i] + p[i+1]
print(sum(d))