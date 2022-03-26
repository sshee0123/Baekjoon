# 11557
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    max_alcho = 0
    max_univ = ""
    for _ in range(n):
        univ, alcho = sys.stdin.readline().split()
        alcho = int(alcho)
        if alcho>max_alcho:
            max_alcho = alcho
            max_univ = univ
    print(max_univ)