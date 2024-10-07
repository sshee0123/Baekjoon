import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memo = dict()
for _ in range(n):
    memo[input().rstrip()] = 1
answer = n

for _ in range(m):
    blog = list(input().rstrip().split(','))
    for k in blog:
        if k in memo.keys() and memo[k] == 1:
            memo[k] -=1
            answer -=1
    print(answer)