n = int(input())
cine = input()
lcnt = cine.count('LL')
scnt = cine.count('S')

if lcnt>0:
    print(scnt+lcnt+1)
else:
    print(scnt)
