import sys
import heapq
n = int(input())
s=[]
result = []
start =0

# for i in range(n):
#     s.append(int(sys.stdin.readline()))
# if n==1:
#     print(0)
# else:
#     s.sort()
#     for i in range(n-1):
#         start = sum(s[0:i+2])
#         result.append(start)
# print(sum(result))

for i in range(n):
    heapq.heappush(s,int(sys.stdin.readline()))
if len(s)==1:
    print(0)
else:
    ans = 0
    while len(s)>1:
        tmp_1 = heapq.heappop(s)
        tmp_2 = heapq.heappop(s)
        ans+=tmp_1+tmp_2
        heapq.heappush(s,tmp_1+tmp_2)

    print(ans)