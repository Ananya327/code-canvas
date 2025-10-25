def isValid(s):
    stack = []  # to store opening brackets
    for ch in s:
        if ch in "({[":       # if opening bracket
            stack.append(ch)
        else:                 # closing bracket
            if not stack:     # nothing to match
                return False
            last = stack.pop()   # take last opening
            if ch == ')' and last != '(':
                return False
            if ch == ']' and last != '[':
                return False
            if ch == '}' and last != '{':
                return False
    
    return not stack  # True if empty (all matched)
  

# Examples:
print(isValid("())"))       # True

