s = list(input())
s.sort(reverse=True)
sum = 0
for i in s:
    sum+=int(i)
if sum % 3 ==0 and '0' in s:
    print(''.join(s))
else:
    print(-1)