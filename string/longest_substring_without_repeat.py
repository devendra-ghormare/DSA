def longestSubstring(s:str):
    n  = len(s)

############# Brute Force ##############
    # max_len = 0
    # for i in range(n):
    #     count = 0
    #     seen = []
    #     for j in range(i, n):
    #         if s[j] not in seen:
    #             seen.append(s[j])
    #             count += 1
    #             max_len = max(max_len, count)
    #         else:
    #             break
    # return max_len

######### Optimal sliding window #########
    left = 0
    seen = set()
    max_len = 0

    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(longestSubstring(s = "abcabcbb"))