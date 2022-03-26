# 1476

import sys
e, s, m = map(int,sys.stdin.readline().split())
cnt = 1
starte, starts, startm = 1,1,1
while True:
    if starte == e and starts == s and startm == m:
        break
    starte += 1
    starts += 1
    startm += 1
    cnt += 1
    if starte > 15:
        starte = 1
    if starts > 28:
        starts = 1
    if startm > 19:
        startm = 1

print(cnt)

