from itertools import product
def solution(word):
    answer = 0
    dictionary = ['A','E','I','O','U']
    my_dic = []
    for i in range(1,6):
        for j in product(dictionary,repeat = i):
            my_dic.append(''.join(j))
    my_dic.sort()
    answer = my_dic.index(word)+1
    return answer