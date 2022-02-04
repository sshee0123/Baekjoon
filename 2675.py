import sys
T = int(input())
for i in range(T):
    R, S = sys.stdin.readline().split()
    text = ''
    for j in S:
        text+=int(R)*j
    print(text)