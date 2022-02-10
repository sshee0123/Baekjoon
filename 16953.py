from collections import deque
A,B = map(int,input().split())
# cnt = 1
# while True:
#     if B==A:
#         break
#     if (B%2!=0 and B%10!=1) or B<A:
#         cnt=-1
#         break
#     else:
#         if B%10==1:
#             B=B//10
#             cnt += 1
#         else:
#             B=B//2
#             cnt+=1
# print(cnt)

res = -1
q = deque()
q.append([A,1])
while q:
    n,cnt = q.popleft()
    if n==B:
        res = cnt
        break
    if n*2<=B:
        q.append([n*2,cnt+1])
    if int(str(n)+"1")<=B:
        q.append([int(str(n)+"1"),cnt+1])
print(res)
