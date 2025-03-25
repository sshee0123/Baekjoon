def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
        
def solution(n, costs):
    answer = 0
    costs = sorted(costs,key=lambda x: x[2])
    global parent
    parent = [i for i in range(n)]
    for a,b,w in costs:
        if find(a)!=find(b):
            answer += w
            union(a,b)
    return answer