N = int(input())
cnt = 0

while N>=0:
    #5의 배수면 5로 나누고
    if N%5 ==0:
        cnt+= N//5
        print(cnt)
        break
    #5의 배수가 아니면 5의 배수가 될때까지 3
    N-=3
    cnt+=1

else:
    print(-1)