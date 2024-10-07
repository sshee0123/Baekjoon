import sys
input = sys.stdin.readline

p, m = map(int,input().split())
room = []

for _ in range(p):
    lv, n = input().split()
    lv = int(lv)
    if room == []: # 매칭방이 없으면 생성
        room.append([(lv, n)])
    else:
        for r in room:
            if (r[0][0]-10 <= lv <= r[0][0]+10) and len(r) < m:
                r.append((lv, n))
                break
        else:
            room.append([(lv, n)])

for r in room:
    r.sort(key=lambda x:x[1])
    if len(r) == m:
        print("Started!")
        for i, j in r:
            print(i,j)
    else:
        print("Waiting!")
        for i, j in r:
            print(i,j)