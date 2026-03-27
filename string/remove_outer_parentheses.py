def removeParentheses(s):
    depth = 0
    result = []

    for char in s:
        if char == "(":
            if depth > 0:
                result.append(char)
            depth += 1
        else:
            depth -= 1
            if depth > 0:
                result.append(char)
    
    return "".join(result)


print(removeParentheses("(()())(())"))
print(removeParentheses("(()())(())(()(()))"))