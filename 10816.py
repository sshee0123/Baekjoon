import sys
from collections import Counter
N = int(input())
card = list(map(int,sys.stdin.readline().split()))
M = int(input())
check = list(map(int,sys.stdin.readline().split()))
card.sort()
#
#이진탐색 -> 시간초과!!!!
# def binary_search(target,arr):
#     start = 0
#     end = N-1
#     while start<=end:
#         mid = (start+end)//2
#         if arr[mid] == target:
#             return arr.count(arr[mid])
#         elif arr[mid] < target:
#             start = mid+1
#         else:
#             end = mid-1
#     return 0
#
# for i in check:
#     print(binary_search(i,card),end=' ')

#Counter 내장함수
cnt = Counter(card)
for i in range(len(check)):
    if check[i] in cnt:
        print(cnt[check[i]],end=' ')
    else:
        print(0,end=' ')
print()
#딕셔너리사용
dic = {}
for i in card:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
for i in check:
    if i in dic:
        print(dic[i],end=' ')
    else:
        print(0,end=' ')