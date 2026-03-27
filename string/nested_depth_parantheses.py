def maxDepth(s:str):

    max_d = 0
    count = 0

    for ch in s:
        if ch == "(":
            count += 1
            max_d = max(max_d, count)
        elif ch == ")":
            count -= 1
    
    return max_d

print(maxDepth("(1+(2*3)+((8)/4))+1"))
print(maxDepth("(1)+((2))+((3))"))
print(maxDepth("()(())((()()))"))
