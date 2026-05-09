def removeElement(nums, val):
    non_k_ind = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[non_k_ind], nums[i] = nums[i], nums[non_k_ind]
            non_k_ind += 1
            
    
    return non_k_ind

print(removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))
print(removeElement(nums = [3,2,2,3], val = 3))
    

