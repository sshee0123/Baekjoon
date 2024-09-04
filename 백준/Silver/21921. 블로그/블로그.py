import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visits = list(map(int, input().split()))
answer = sum(visits[:x]) #초기 비교값
cnt = 1 #방문자수

tmp = answer
for i in range(x,n):
    #슬라이딩
    tmp -= visits[i-x]
    tmp += visits[i]
    if answer < tmp: #비교값보다 더 큰 방문자수가 나오면 갱신
        answer = tmp
        cnt = 1
    elif answer == tmp:
        cnt += 1
if answer == 0:
    print("SAD")
else:
    print(answer)
    print(cnt)