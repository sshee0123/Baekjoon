# 1748
import sys
n = sys.stdin.readline().rstrip()
len_n = len(n)
n = int(n)
answer = 0
base = 0

for i in range(len_n-1):
    base += 9*(10**i)*(i+1)
answer = base + (n-10**(len_n-1)+1)*(len_n)
print(answer)
