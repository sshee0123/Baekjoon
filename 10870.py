# n = int(input())
#
# # #재귀함수
# # def fib(n):
# #     if n<=1:
# #         return n
# #     return fib(n-1)+fib(n-2)
# # print(fib(n))
#
# #반복문
# fib = [0,1]
# for i in range(2,n+1):
#     num = fib[i-1]+fib[i-2]
#     fib.append(num)
# print(fib[n])

import sys
n = int(input())
print(sum(map(int,sys.stdin.readline().strip())))