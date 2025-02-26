def solution(money):
    answer = []
    tmp1=tmp2=money
    coffee = tmp1 // 5500
    re_money = tmp2 - (coffee*5500)
    answer.append(coffee)
    answer.append(re_money)
    return answer