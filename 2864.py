A,B = input().split()
MAX = int(A.replace('5','6'))+int(B.replace('5','6'))
MIN = int(A.replace('6','5'))+int(B.replace('6','5'))
print(MAX,MIN)