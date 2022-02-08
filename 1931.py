N = int(input())
time_table = []
for i in range(N):
    s,e = map(int,input().split())
    time_table.append([s,e])

# time_table.sort()
time_table = sorted(time_table,key=lambda a:a[0])
time_table = sorted(time_table,key=lambda a:a[1])

end = 0
cnt = 0
for s,e in time_table:
    if s>=end:
        cnt+=1
        end = e

print(cnt)