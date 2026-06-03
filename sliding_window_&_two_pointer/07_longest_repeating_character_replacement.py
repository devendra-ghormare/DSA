def characterReplacement(s, k):
    n = len(s)
    max_len = 0

################# Brute Force ################
  
    # for i in range(n):
    #     freq = [0] * 26
    #     max_freq = 0

    #     for j in range(i, n):
    #         freq[ord(s[j]) - ord('A')] += 1

    #         max_freq = max(max_freq, freq[ord(s[j]) - ord('A')])

    #         window_len = j - i + 1

    #         replace = window_len - max_freq

    #         if replace <=k :
    #             max_len = max(max_len, window_len)
    
    # return max_len

    # Time: O(n²)
    # Space: O(1)

##################### Optimal solution #######################
    max_freq = 0
    freq = [0] * 26
    l = 0
    r = 0

    while r < n:
        freq[ord(s[r]) - ord('A')] += 1

        max_freq = max(max_freq, freq[ord(s[r]) - ord('A')])

        while (r - l + 1) - max_freq > k:
            freq[ord(s[l]) - ord('A')] -= 1
            max_freq = max(freq)
            l += 1
        
        if (r - l + 1) - max_freq <= k:
            max_len = max(max_len, r-l+1)
        
        r += 1

    return max_len

    # Time: O(26 * n) = O(n)
    # Space = O(1)

s = "AABABBA"
k = 1
print(characterReplacement(s, k))