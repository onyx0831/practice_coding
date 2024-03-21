from collections import deque
N = int(input())
S = str(input())
ans_s = deque()

depth = 0

for s in S:
    if s == '(':
        
        ans_s.append(s)
        depth += 1

    elif s == ')':
        if depth:
            while ans_s:
                a = ans_s.pop()
                if a == '(':
                    break
            depth -= 1
            
        else:
            ans_s.append(s)

    else:
        ans_s.append(s)

print(''.join(ans_s))
