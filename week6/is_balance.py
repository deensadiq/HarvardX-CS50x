def is_balanced(parenthesis):
    stack = []
    opening = set(('(', '[', '{'))
    closing = set({')', ']', '}'})
    pairs = dict({
        ')': '(',
        ']': '[',
        '}': '{'
    })
    
    for c in parenthesis:
        if c in opening:
            stack.append(c)
        elif c in closing:
            print(pairs[c])
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
            
    print(opening)
    print(closing)
    print(pairs)
    return print(stack)

print(is_balanced("thisisacomplex(example)fortest]"))
            