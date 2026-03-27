import heapq
from collections import Counter
def tokFrequestElement(nums, k):

############## Brute Force ##################

    # freq = {}
    # result = []

    # for num in nums:
    #     freq[num] = freq.get(num, 0) + 1
    
    # sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    # for i in range(k):
    #     result.append(sorted_freq[i][0])
    
    # return result

############## Optimal solution ###############
    # freq = Counter(nums)

    # return heapq.nlargest(k, freq.keys(), key=freq.get)

############### One more optimal ###############
    freq = {}
    result = []

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        bucket[count].append(num)
    
    print(bucket)
    
    for i in range(len(nums), 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
    
nums = [1,1,1,1,2,2,2,3,3]
print(tokFrequestElement(nums, 2))
