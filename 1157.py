S = input().upper()
words = list(set(S))
cnt_list = []

for i in words:
    cnt = S.count(i)
    cnt_list.append(cnt)
if cnt_list.count(max(cnt_list))>1:
    print("?")
else:
    max_index = cnt_list.index(max(cnt_list))
    print(words[max_index])