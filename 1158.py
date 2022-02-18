import sys
n,k = map(int,sys.stdin.readline().split())
q=[]
result = []
for i in range(1,n+1):
    q.append(i)

index = 0
while q:
    index += k-1
    if index >= len(q):
        index = index % len(q)

    result.append(q.pop(index))

print("<", ', '.join(str(i) for i in result),">",sep="")