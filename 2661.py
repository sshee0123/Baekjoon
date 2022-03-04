# import sys
#
# def possible(arr):
#     idx = len(arr)
#     for i in range(1,(idx//2)+1):
#         if arr[-i:] == arr[-i*2:-i]:
#             return False
#     return True
# def solution(arr,depth):
#     if depth == n:
#         print(arr)
#     for i in range(1,4):
#         arr.append(i)
#         if possible(arr):
#
#
# n = int(sys.stdin.readline())
# solution([1],1)