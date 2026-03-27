def longestPalindrom(s:str):
    n = len(s)

########### Brute Force ############
    # result = ""
    # for i in range(n):
    #     for j in range(i, n):
    #         substring = s[i:j+1]
    #         if substring == substring[::-1]:
    #             if len(substring) > len(result):
    #                 result = substring
    
    # return result

########### Optimal approach ############
    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    result = ""
    for i in range(n):
        p1 = expand(i, i)
        p2 = expand(i, i+1)

        result = max(result, p1, p2, key=len)
    return result


print(longestPalindrom("babad"))