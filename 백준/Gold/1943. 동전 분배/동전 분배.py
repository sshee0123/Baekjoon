#1943
import sys
for _ in range(3):
    n = int(sys.stdin.readline())
    coins = {}
    target = 0
    for _ in range(n):
        coin, cnt = map(int, sys.stdin.readline().split())
        coins[coin] = cnt
        target += coin*cnt

    if target & 1:
        print(0)
        continue
    target = target//2
    dp = [1] + [0]*target
    for coin in coins:
        for money in range(target, coin-1, -1):
            if dp[money-coin]:
                for j in range(coins[coin]): # 동전 개수만큼
                    if money + coin*j <= target:
                        dp[money + coin*j] = 1
    print(dp[target])