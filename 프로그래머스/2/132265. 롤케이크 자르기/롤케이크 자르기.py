from collections import Counter
def solution(topping):
    answer = 0
    a_dic = Counter(topping)
    b_dic = set() # 나눠준 토핑 중복제거 set
    for t in topping:
        a_dic[t] -= 1 # 나눠주기
        b_dic.add(t)
        if a_dic[t] == 0: # 다 나눠주면 뺴기
            a_dic.pop(t)
        if len(a_dic) == len(b_dic):
            answer += 1
        # print(a_dic,b_dic)       
    return answer