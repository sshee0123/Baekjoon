# 2884
import sys
h,m = map(int,sys.stdin.readline().split())
# 45가 기준
if m>44:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m+15)
else: # h==0
    print(23, m+15)