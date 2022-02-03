n = int(input())

#재귀함수
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(n))

#반복문
fib_for = [0,1]
for i in range(2,n+1):
    n = fib_for[n-1]+fib_for[n-2]
    fib_for.append(n)
print(fib_for[n])