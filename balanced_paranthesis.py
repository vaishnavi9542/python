def bal_paran(s):
    stack = []
    parenthesis = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in parenthesis.values():
            stack.append(char)
        elif char in parenthesis.keys():
            if not stack or stack[-1] != parenthesis[char]:
                return False
            stack.pop()

    return len(stack) == 0

s = input()
print(bal_paran(s))
