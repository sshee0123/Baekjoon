C = int(input())
coins = [500,100,50,10,5,1]
money = 1000-C
cnt=0
for c in coins:
    cnt+=money//c
    money%=c
print(cnt)



