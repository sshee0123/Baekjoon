T = int(input())
# btn = [300,60,10]
# result = [0,0,0]
# for i in range(3):
#     while btn[i]<=T:
#         T-=btn[i]
#         result[i] +=1
#
# if T!=0:
#     print(-1)
# else:
#     for i in result:
#         print(i,end=' ')

if T%10!=0:
    print(-1)
else:
    A=B=C=0
    A = T//300
    B = (T%300)//60
    C = (T%300)%60//10
    print(A,B,C)