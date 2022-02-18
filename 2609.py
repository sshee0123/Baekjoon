import math
import sys
a,b = map(int,sys.stdin.readline().split())
# print(math.gcd(a,b))
# print(math.lcm(a,b))

def GCD(a,b):
    while b>0:
        a,b = b, a%b
    return a
def LCM(a,b):
    return int(a*b / GCD(a,b))
print(GCD(a,b))
print(LCM(a,b))