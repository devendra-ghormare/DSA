def count_presence(nums):
    count  = {}

    for num in nums:
        if num  in count:
            count[num] += 1
        else:
            count[num] = 1

    return count
    # result = []
    # for key, value in count.items():
    #     result.append([key, value])
    
    # return result

print(count_presence([1,2,2,1,3,4]))


