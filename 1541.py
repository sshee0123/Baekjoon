s = input().split('-')
result = []
for i in s:
    cnt = 0
    plus = i.split('+')
    for p in plus:
        cnt+=int(p)
    result.append(cnt)

answer = result[0]
for i in range(1,len(result)):
    answer-=result[i]
print(answer)