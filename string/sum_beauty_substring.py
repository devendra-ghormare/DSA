def beautySum(s:str) -> int:
    n = len(s)
    total = 0

########## Brute Force #############
    # for i in range(n):
    #     for j in range(i, n):
    #         count = {}
    #         for k in range(i, j+1):
    #             count[s[k]] = count.get(s[k], 0) + 1
            
    #         total += (max(count.values()) - min(count.values()))
    
    # return total

######### Optimal approach ##########
    for i in range(n):
        count = {}
        for j in range(i, n):
            count[s[j]] = count.get(s[j], 0) + 1
            total += (max(count.values()) - min(count.values()))
            
    return total

print(beautySum(s = "aabcb"))
print(beautySum(s = "aabcbaa"))