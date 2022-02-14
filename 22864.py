A,B,C,M = map(int,input().split())
p=0
w=0
if A>M:
    print(0)
else:
    for i in range(1,25):
        if p+A <= M:
            p+=A
            w+=B
        else:
            if p-C<0:
                p=0
            else:
                p-=C
    print(w)
