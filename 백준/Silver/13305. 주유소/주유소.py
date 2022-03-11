n = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))

result = 0
now_price = price[0]
for i in range(n-1):
    if price[i]<now_price:
        now_price=price[i]
    result += now_price * road[i]
print(result)