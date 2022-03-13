# 12865
# 냅색 알고리즘
import sys
n, k = map(int,sys.stdin.readline().split())
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]
stuff = [[0,0]]
for _ in range(n):
    stuff.append(list(map(int,sys.stdin.readline().split())))

for i in range(n+1):
    for j in range(k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight: # 버틸 수 있는 무게가 현재 무게보다 작다면 전에 있는 값 그대로
            knapsack[i][j] = knapsack[i-1][j]
        else:
            # max( 현재 물건을 넣어주고 남은 무게를 채울 수 있는 최대값 / 다른 물건들로 채우는 값 )
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack[n][k])