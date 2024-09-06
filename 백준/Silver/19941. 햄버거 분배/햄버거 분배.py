import sys
input = sys.stdin.readline

n, k = map(int, input().split())
desk = list(input().strip())
cnt = 0
for i in range(n):
    if desk[i] == "P":
        for j in range(i-k, i+k+1):
            if -1 < j < n:
                if desk[j] == 'H':
                    desk[j] = 'X'
                    cnt += 1
                    break
print(cnt)