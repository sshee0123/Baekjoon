T = int(input())
coins = [25,10,5,1]
for i in range(T):
    result = ""
    C = int(input())
    for coin in coins:
        result+=str(C//coin)+" "
        C%=coin
    print(result)
