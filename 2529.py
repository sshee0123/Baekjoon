k = int(input())
oper = input().split()
visited = [0]*10
r_max, r_min = "",""

def giveAnswer(op,i,j):
    if op==">":
        return i>j
    else:
        return i<j
    return

def dfs(cnt,s):
    global r_max,r_min
    if cnt==k+1:
        if len(r_min)==0:
            r_min = s
        else:
            r_max = s
        return
    for i in range(10):
        if not visited[i]:
            if cnt==0 or giveAnswer(oper[cnt-1],s[-1],str(i)):
                visited[i] = 1
                dfs(cnt+1, s+str(i))
                visited[i] = 0

dfs(0,"")
print(r_max)
print(r_min)
