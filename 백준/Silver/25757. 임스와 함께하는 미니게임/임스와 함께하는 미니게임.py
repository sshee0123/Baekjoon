import sys
n, g = input().split()
player = set()
for _ in range(int(n)):
    player.add(sys.stdin.readline().strip())
k = len(player)

if g == "Y":
    print(k)
elif g == "F":
    print(k//2)
elif g == "O":
    print(k//3)