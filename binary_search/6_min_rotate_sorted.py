def minRotateSorted(nums):
        n = len(nums)
        low = 0
        high = n - 1
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2

            # optimal: check for duplicate elements in array  
            if nums[low] == nums[mid] == nums[high]:
                ans = min(ans, nums[low])
                low += 1
                high -= 1
                continue

            if nums[low] <= nums[mid]:
                ans = min(ans, nums[low])
                low = mid + 1
            else:
                ans = min(ans, nums[mid])
                high = mid - 1

        return ans

print(minRotateSorted([3,4,5,1,2]))