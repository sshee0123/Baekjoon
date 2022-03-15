# 11005
import sys
alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int,sys.stdin.readline().split())
answer = ''
while n!=0:
    answer += alpha[n % b]
    n //= b
print(answer[::-1])

