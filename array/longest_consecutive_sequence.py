def longest_consecutive_sequence(nums):
    n = len(nums)

    ######## Brute force by checkin i+1 present in array ####
    # longest = 0

    # for i in range(n):
    #     current = nums[i]
    #     count = 1

    #     while current + 1 in nums:
    #         current += 1
    #         count += 1
        
    #     longest = max(longest, count)

    # return longest


    ######### Better solution with sorted and then calculation ######
    # nums = sorted(nums)
    # lastSmaller = float('-inf')
    # largest = 1
    # count = 0

    # for i in range(n):
    #     if nums[i] - 1 == lastSmaller:
    #         count += 1
    #         lastSmaller = nums[i]
    #     elif nums[i] != lastSmaller:
    #         count = 1
    #         lastSmaller = nums[i]
        
    #     largest = max(largest, count)

    # return largest

    ######## Optimal solution with puting in set ######33

    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            current = num
            count = 1

            while current + 1 in nums_set:
                current += 1
                count += 1

            longest = max(longest, count)
    return longest

print(longest_consecutive_sequence([100,4,200,1,3,2]))
print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))