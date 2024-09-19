import sys
input = sys.stdin.readline

n = int(input())
target = list(input().strip()) #첫 번째 단어
answer = 0
for _ in range(n-1):
    tg = target[:]
    word = input().strip()
    cnt = 0
    # print("전", tg)
    # print("전", cnt)
    for w in word:
        if w in tg:
            tg.remove(w)
        else:
            cnt += 1
    # print("후", tg)
    # print("후", cnt)
    if cnt < 2 and len(tg) < 2:
        answer += 1
print(answer)