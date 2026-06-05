def atMost(nums, k):
    if k < 0:
        return 0
    
    count = 0
    array_sum = 0
    left = right = 0

    while right < len(nums):
        array_sum += (nums[right] % 2)

        while array_sum > k:
            array_sum -= (nums[left] % 2)
            left += 1
        
        count += right - left + 1
        right += 1
    
    return count

def numOfNiceSubarrays(nums, k):
    return atMost(nums, k) - atMost(nums, k-1)

# Time: O(n)
# Space: O(1)

print(numOfNiceSubarrays(nums = [1,1,2,1,1], k = 3))