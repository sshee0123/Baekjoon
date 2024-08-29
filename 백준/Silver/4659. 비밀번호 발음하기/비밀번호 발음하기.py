
spec = ['a', 'e', 'i', 'o', 'u'] #모음
accept = ['ee', 'oo'] #예외

while True:
    pwd = input()
    if pwd == "end":
        break
    f1=f2=0 #3개체크 flag, 2개체크 flag
    # 모음 하나라도 없으면 안됨
    cnt = 0
    for p in pwd:
        if p in spec:
            cnt += 1
    if cnt < 1:
        print(f'<{pwd}> is not acceptable.')
        continue
    # 연속3개 자음이거나 모음이면 안됨.
    for i in range(len(pwd)-2):
        if pwd[i] in spec and pwd[i+1] in spec and pwd[i+2] in spec:
            f1 = 1
        elif pwd[i] not in spec and pwd[i+1] not in spec and pwd[i+2] not in spec:
            f1 = 1
    if f1 == 1:
        print(f'<{pwd}> is not acceptable.')
        continue
    #2개가 연속해서 같으면 예외상황이면 가능, 아니면 불가능.
    for i in range(len(pwd)-1):
        if pwd[i] == pwd[i+1]:
            if (pwd[i]+pwd[i+1]) in accept:
                continue
            else:
                f2 = 1
    if f2 == 1:
        print(f'<{pwd}> is not acceptable.')
        continue
    print(f'<{pwd}> is acceptable.')