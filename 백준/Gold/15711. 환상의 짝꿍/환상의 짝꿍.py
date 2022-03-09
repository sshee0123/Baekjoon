#15711
import sys

# 에라토스테네스의 체
# n = 2*(10**12) +1 # 끈의 길이 메모리 초과 따라서 절반만 에라토스테네스의 체 수행
n = 2*(10**6) + 1
arr = [True for _ in range(n)]
primes = [] # 소수
for i in range(2,n):
    if arr[i]:
        primes.append(i)
        for j in range(2*i, n, i):
            arr[j] = False

# 소수인지 판별
def isPrime(x):
    if x > n: # x 가 n인 2*10**12 보다 크면
        for prime in primes:
            if prime >= x:
                break
            elif x % prime == 0:# 소수로 나뉘는지로 판별
                return False
        return True
    else: # x가 n보다 작으면 바로 소수에서 꺼내기
        return arr[x]

# 테스트케이스
t = int(sys.stdin.readline())
for _ in range(t):
    ab = sum(map(int,sys.stdin.readline().split()))

    # 골드바흐의 추측 : 4보다 큰 짝수는 두 홀수 소수의 합으로 가능하다.
    # 4 보다 작으면 NO
    if ab < 4 :
        print("NO")
    # 4보다 큰 짝수 YES
    elif ab % 2 == 0:
        print("YES")
    else: # 홀수는 2(짝수 소수) + 홀수 소수의 합으로 가능하다. -> 홀수-2 가 소수인지 확인
        if isPrime(ab-2):
            print("YES")
        else:
            print("NO")



