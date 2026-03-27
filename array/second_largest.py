# def secondLargestElement(nums):
#         largest = float('-inf')
#         for i in range(len(nums)):
#             if nums[i] > largest:
#                 largest = nums[i]
        
#         slargest = float('-inf')

#         for i in range(len(nums)):
#             if nums[i] > slargest and nums[i] != largest:
#                 slargest = nums[i]
        
#         return slargest

# print(secondLargestElement([8, 8, 7, 6, 5]))

########### OPtimumn answer

def secondLargestElement(nums):
    largest = nums[0]
    slargest = -1

    for i in range(len(nums)):
            if nums[i] > largest:
               slargest = largest
               largest = nums[i]
            elif nums[i] < largest and nums[i] > slargest:
                slargest = nums[i]
    return slargest

print(secondLargestElement([8, 8, 7, 6, 5]))