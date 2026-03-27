
def frequencySort(s:str):

########## Brute Force ###########
    # freq = {}
    # res = ""
    
    # for ch in s:
    #     if ch in freq:
    #         freq[ch] += 1
    #     else:
    #         freq[ch] = 1
    
    # max_freq = 0

    # for ch in freq:
    #     if freq[ch] > max_freq:
    #         max_freq = freq[ch]
    
    # for i in range(max_freq, 0, -1):
    #     for ch in freq:
    #         if freq[ch] == i:
    #             res += ch * i
    
    # return res

########## Optimal solution ###########
    freq = {}
    bucket = [[] for _ in range(len(s) + 1)]
    res = ""
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    for key, val in freq.items():
        bucket[val].append(key)
    
    for i in range(len(s), 0, -1):
        for ch in bucket[i]:
            res += ch * i

    return res


print(frequencySort("aaabcc"))