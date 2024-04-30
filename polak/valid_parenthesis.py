def is_valid(s: str) -> bool:
    stack = []
    bracket_map = {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in bracket_map:
            stack.append(c)
        
        elif not stack or bracket_map[stack.pop()] != c:
            return False
        
    return not stack


print(is_valid("(]"))