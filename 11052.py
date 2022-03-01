import sys
n = int(sys.stdin.readline())
price = [0] + list(map(int,sys.stdin.readline().split()))
d = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i] = max(price[j]+d[i-j], d[i])
print(d[n])