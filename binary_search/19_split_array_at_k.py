def count_required_partitions(numbers, max_allowed_sum):
    """
    Returns how many subarrays (partitions) are needed
    if no partition has sum greater than max_allowed_sum.
    """
    partitions = 1
    current_sum = 0

    for value in numbers:
        if current_sum + value <= max_allowed_sum:
            current_sum += value
        else:
            partitions += 1
            current_sum = value

    return partitions


def split_array_min_largest_sum(nums, k):
    """
    Splits the array into k continuous subarrays such that
    the largest subarray sum is minimized.
    """
    if k > len(nums):
        return -1

    left = max(nums)     
    right = sum(nums)    

    while left <= right:
        mid = (left + right) // 2

        required_partitions = count_required_partitions(nums, mid)

        if required_partitions > k:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Example
nums = [25, 46, 28, 49, 24]
k = 4

print(split_array_min_largest_sum(nums, k))
