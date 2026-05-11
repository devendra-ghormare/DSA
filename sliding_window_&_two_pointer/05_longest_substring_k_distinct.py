def longestSubstringKDistinct(s:str, k:int) -> int:
    n = len(s)
    maxlen = 0
    freq = {}

######################## Brute Force ####################
    # for i in range(n):
    #     freq.clear()
    #     for j in range(i, n):
    #         freq[s[j]] = freq.get(s[j], 0) + 1

    #         if len(freq) <= k:
    #             maxlen = max(maxlen, j-i+1)
    #         else:
    #             break
        
    #     return maxlen
    
    # Time: O(n²)
    # Space: O(1)      

######################## Optimal solution ##################
    left = right = 0


    while right < n:
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1

            if freq[s[left]] == 0:
                del freq[s[left]]

            left += 1

        maxlen = max(maxlen, right - left + 1)
        right += 1

    return maxlen

    # Time = O(n)
    # Space = O(1)


print(longestSubstringKDistinct("aaabbccd", 2))
