from collections import deque

parentheses = deque([el for el in input()])

is_balanced = False

while parentheses:

    if len(parentheses) == 2:
        first = parentheses.popleft()
        second = parentheses.pop()
        if first == '(':
            if second == ')':
                is_balanced = True
            else:
                is_balanced = False
                break
        elif first == '[':
            if second == ']':
                is_balanced = True
            else:
                is_balanced = False
                break
        elif first == '{':
            if second == '}':
                is_balanced = True
            else:
                is_balanced = False
                break
        else:
            is_balanced = False
            break
    else:

        first = parentheses.popleft()
        second = parentheses.popleft()
        last = parentheses.pop()

        if first == '(':
            if second == ')':
                is_balanced = True
                parentheses.append(last)
            elif last == ')':
                is_balanced = True
                parentheses.appendleft(second)
            else:
                is_balanced = False
                break
        elif first == '[':
            if second == ']':
                is_balanced = True
                parentheses.append(last)
            elif last == ']':
                is_balanced = True
                parentheses.appendleft(second)
            else:
                is_balanced = False
                break
        elif first == '{':
            if second == '}':
                is_balanced = True
                parentheses.append(last)
            elif last == '}':
                is_balanced = True
                parentheses.appendleft(second)
            else:
                is_balanced = False
                break
        else:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
