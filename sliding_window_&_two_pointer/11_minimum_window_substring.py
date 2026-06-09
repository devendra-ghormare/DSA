def minWindowSubstring(s:str, t:str):
#################### Brute Force ####################

    # min_len = float('inf')
    # s_index = -1

    # for i in range(len(s)):
    #     hash = [0]*256
    #     count = 0
    #     for j  in t:
    #         hash[ord(j)] += 1
        
    #     for j in range(i, len(s)):
    #         hash[ord(s[j])] -= 1
    #         if hash[ord(s[j])] > 0:
    #             count += 1
    #             

#             if count == len(t):
#                 if j-i+1 < min_len:
#                     min_len = j-i+1
#                     s_index = i
#                 break
    # if s_index == -1:
    #     return ""
    
    # return s[s_index:s_index + min_len]

    # Time: O(n²)
    # Space: O(n)

##################### Optimal solution ####################
    # n = len(s)
    # m = len(t)
    # left = right = 0
    # min_len = float('inf')
    # hash = [0] * 256
    # s_index = -1
    # count = 0

    # for i in t:
    #     hash[ord(i)] += 1
    
    # while right < n:
    #     if hash[ord(s[right])] > 0:
    #         count += 1

    #     hash[ord(s[right])] -= 1

    #     while count == m:
    #         if right-left+1 < min_len:
    #             min_len = right-left + 1
    #             s_index = left
            
    #         hash[ord(s[left])] += 1
    #         if hash[ord(s[left])] > 0:
    #             count -= 1
    #         left += 1
        
    #     right += 1
    # return "" if s_index == -1 else s[s_index:s_index+min_len]

    # Time: O(n)
    # Space: O(n)

############ Dictionary version ################
    n = len(s)
    m = len(t)
    left = right = 0
    start = -1
    min_len = float('inf')
    count = 0
    mpp = {}

    for char in t:
        mpp[char] = mpp.get(char, 0) + 1
    
    while right < n:
        if mpp.get(s[right], 0) > 0:
            count += 1
        mpp[s[right]] = mpp.get(s[right], 0) - 1

        while count == m:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left
            
            mpp[s[left]] = mpp.get(s[left], 0) + 1
            if mpp[s[left]] > 0:
                count -= 1
            left += 1
        right += 1
        
    return "" if start == -1 else s[start:start+min_len] 

    # Time: O(n)
    # Space: O(n)


print(minWindowSubstring(s = "ADOBECODEBANC", t = "ABC"))
