def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        stack = []
        for i in range(len(s)):
            if len(stack)>0:
                if s[i] == ')' and stack[-1] == '(': stack.pop()
                elif s[i] == '}' and stack[-1] == '{': stack.pop()
                elif s[i] == ']' and stack[-1] == '[': stack.pop()
                else: stack.append(s[i])
            else:
                stack.append(s[i])
        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))    
    return answer