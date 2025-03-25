def solution(rsp):
    answer = ''
    winner = {'2':'0', '0':'5', '5':'2'}
    for r in rsp:
        answer += winner[r]
    return answer