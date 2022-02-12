import sys
n = int(input())
cnt = [0]*(10000+1)

for i in range(n):
    cnt[int(sys.stdin.readline())] +=1
for i in range(len(cnt)):
    for j in range(cnt[i]):
        print(i)
