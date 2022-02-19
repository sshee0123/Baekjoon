import math
import sys
n = int(sys.stdin.readline())
tree = []
bet_tree = []
result = 0

#가로수 저장
for i in range(n):
    tree.append(int(sys.stdin.readline().rstrip()))
#가로수 간격 저장
for i in range(n-1):
    bet_tree.append(tree[i+1]-tree[i])

#가로수 간격의 최대공약수 찾기
gcd = bet_tree[0]
for i in range(1,len(bet_tree)):
    gcd = math.gcd(gcd,bet_tree[i])

#가로수 간격 //최대공약수 -1 의 합이 답
for i in range(len(bet_tree)):
    result += bet_tree[i] // gcd -1
print(result)