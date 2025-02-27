import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    day = int(input())
    price = list(map(int, input().split()))
    money = 0
    maxPrice = 0
    # 거꾸로 탐색
    for i in range(len(price)-1,-1,-1):
        if maxPrice < price[i]:
            maxPrice = price[i]
        else:
            money += maxPrice-price[i]
    print(money)