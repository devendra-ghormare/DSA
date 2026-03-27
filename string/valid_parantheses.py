def validParantheses(s:str):

########## Brute Force ########

    # prev_len = -1

    # while prev_len != len(s):
    #     prev_len = len(s)

    #     s = s.replace("()", "")
    #     s = s.replace("[]", "")
    #     s = s.replace("{}", "")
    
    # return len(s) == 0

#######3 Optimal with stack ########
    stack = []
    pairs = {
        ")":"(",
        "]":"[",
        "}":"{"
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

print(validParantheses("[{()}]"))