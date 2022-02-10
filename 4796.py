import sys
i = 1
while True:
    L,P,V = map(int,sys.stdin.readline().split())
    if L ==0 and P ==0 and V ==0:
        break
    if V%P>=L:
        result = L * (V // P) + L
    else:
        result = L*(V//P)+ (V % P)
    print("Case "+str(i)+": "+str(result))
    i += 1


