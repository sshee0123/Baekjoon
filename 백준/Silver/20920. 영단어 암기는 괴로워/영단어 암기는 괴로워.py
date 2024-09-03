import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = dict()
for _ in range(n):
    tmp = input().strip()
    if len(tmp) >= m:
        if tmp in words:
            words[tmp] += 1
        else:
            words[tmp] = 1
answer = sorted(words.items(), key=lambda x: (-x[1], -(len(x[0])), x[0]))
for i in answer:
    print(i[0])