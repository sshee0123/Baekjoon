# 1725
import sys
n = int(sys.stdin.readline())
h = []
stack = []
result = 0
for _ in range(n):
    h.append(int(sys.stdin.readline()))

for i in range(n):
    while stack and h[stack[-1]] > h[i]:
        height = h[stack[-1]]
        width = i
        stack.pop()
        if stack:
            width = (i-stack[-1]-1)
        result = max(result, width*height)
    stack.append(i)

# 스택이 비어있지 않은 경우
# right 가 가장 오른쪽 끝인 경우
# 스택에 있는 막대 하나씩 빼면서 위의 과정 반복 
while stack:
    height = h[stack[-1]]
    stack.pop()
    width = n
    if stack:
        width = (n-stack[-1]-1)
    result = max(result, width*height)
print(result)