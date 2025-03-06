def solution(k, tangerine):
    answer = 0
    dic = {}
    for tang in tangerine:
        if tang not in dic:
            dic[tang] = 1
        else:
            dic[tang] += 1
    dic = dict(sorted(dic.items(), key = lambda x:x[1], reverse = True))
    for key,val in dic.items():
        if k <=0:
            return answer
        k -= val
        answer += 1
    return answer