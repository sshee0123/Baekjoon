
n = int(input())
arr = []
for i in range(n):
    x,y = map(str,input().split())
    x = int(x)
    arr.append((x,y))
arr.sort(key = lambda a:a[0])
for i in arr:
    print(i[0],i[1])
