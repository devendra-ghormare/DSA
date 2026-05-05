def lengthOfLongestSubstring(s):
    n = len(s)
    hash_arr = [-1] * 256
    left = 0
    maxLen = 0 

    for right in range(n):
        ascii_value = ord(s[right])
        if hash_arr[ascii_value] != -1:
            if hash_arr[ascii_value] >= left:
                left = hash_arr[ascii_value] + 1
        
        hash_arr[ascii_value] = right
        maxLen = max(maxLen, right-left+1)
    
    return maxLen

    # Time = O(n)
    # Space = O(1)


print(lengthOfLongestSubstring("cadbzabcd"))