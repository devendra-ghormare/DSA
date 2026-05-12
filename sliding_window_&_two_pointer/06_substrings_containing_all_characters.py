def numberOfSubstrings(s:str) -> int:
    n = len(s)
    ans = 0

############### Brute Force ################

    # for i in range(n):
    #     count = {'a':0, 'b':0, 'c':0}

    #     for j in range(i, n):
    #         count[s[j]] += 1

    #         if count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
    #             ans += 1
    
    # return ans

    # Time: O(n²)
    # Space: O(1)  

############## Optimal approach ############

    count = {'a':0, 'b':0, 'c':0}
    left = 0

    for right in range(n):
        count[s[right]] += 1

        while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
            ans += n-right

            count[s[left]] -= 1
            left += 1
    
    return ans

    # Time = O(n)
    # Space = O(1)

print(numberOfSubstrings(s = "abcabc"))
print(numberOfSubstrings(s = "aaacb"))
print(numberOfSubstrings(s = "abc"))