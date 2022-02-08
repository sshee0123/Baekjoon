n = int(input())
cost = list(map(int,input().split()))
result = 0
cost.sort()

for i in range(n-1):
    result+=cost[i]
print(result)