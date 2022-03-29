import sys
n = int(sys.stdin.readline())
cnt = 0
for i in range(n):
    s = sys.stdin.readline().rstrip()
    new_word = [s[0]]
    err = 0
    for a in range(len(s)-1):
        if s[a] != s[a+1]:
            if s[a+1] in new_word:
                err += 1
            new_word.append(s[a+1])

    if err == 0:
        cnt += 1
print(cnt)
