import sys
n,k = map(int,sys.stdin.readline().split())
d = [0]*(k+1)
coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))
d[0] = 1
for i in coins:
    for j in range(i,k+1): #동전부터 순회
        if j-i >= 0:
            d[j] += d[j-i]
print(d[k])
