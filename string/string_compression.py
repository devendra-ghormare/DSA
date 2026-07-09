def compress(s:str):
    if not s:
        return ""
    
    count = 1
    result = []

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i] + str(count))
            count = 1
    
    result.append(s[i]+ str(count))

    return "".join(result)

def twoPonter(s):
    n = len(s)
    left = right = 0
    result = []

    while right < n:
        if s[left] == s[right]:
            right += 1
        else:
            result.append(s[left]+str(right-left))
            left = right
    
    result.append(s[left]+str(right-left))

    return "".join(result)
        

# Time = O(n)
# Space = O(n)

print(twoPonter("aaabbc"))
print(compress("sssaaahhh"))