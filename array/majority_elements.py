def majorityElement(nums) -> int:
    n = len(nums)
    target = n // 2

    ######### Brute Force ##########

    # for i in range(n):
    #     count = 0
    #     for j in range(n):
    #         if nums[i] == nums[j]:
    #             num = nums[i]
    #             count += 1
    #         if count > target:
    #             return num

    ######### Better with dict   ##########

    mydict = {}

    for num in nums:
        if num in mydict:
            mydict[num] += 1
        else:
            mydict[num] = 1
    
    for key, value in mydict.items():
        if value > target:
            return key

            
print(majorityElement([2,2,1,1,1,2,2]))