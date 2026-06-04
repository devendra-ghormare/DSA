def atMost(nums, goal):
    if goal < 0:
        return 0

    left = right = 0
    window_sum = 0
    count = 0

    while right < len(nums):
        window_sum += nums[right]

        while window_sum > goal:
            window_sum -= nums[left]
            left += 1

        count += right - left + 1
        right += 1

    return count

def numSubarrayWithSum(nums, goal):
    return atMost(nums, goal) - atMost(nums, goal - 1)

# Time: O(n)
# Space: O(1)

print(numSubarrayWithSum([1,0,1,0,1], goal = 2))

