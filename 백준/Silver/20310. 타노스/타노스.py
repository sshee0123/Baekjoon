import sys
input = sys.stdin.readline

s = list(input().strip())
cnt_0, cnt_1 = s.count('0')//2, s.count('1')//2

# 1은 앞부터 지우고 0은 뒤부터 지우기
cnt = 0
for s1 in s:
    if s1 == '1':
        s.remove(s1)
        cnt += 1
    if cnt == cnt_1:
        break
s = s[::-1] #거꾸로 뒤집기
cnt = 0
for s1 in s:
    if s1 == '0':
        s.remove(s1)
        cnt += 1
    if cnt == cnt_0:
        break

s = s[::-1] #거꾸로 다시 뒤집기
for i in s:
    print(i,end="")
