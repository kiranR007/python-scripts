def is_valid_parentheses(s):
    pairs = {')':"(","]":"[","}":"{"}
    stack =[]
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            # if stack ==[] or not stack or stack.pop() != pairs[ch]:
            if stack ==[] or  stack.pop() != pairs[ch]:
                return False
    return not stack

# print(is_valid_parentheses("{[()]}"))
print(is_valid_parentheses("{[(])}"))
            