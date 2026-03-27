def count_students(nums, pages):
    students = 1
    current_pages = 0

    for length in nums:
        if current_pages + length <= pages:
            current_pages += length
        else:
            students += 1
            current_pages = length
    return students

def findPages(nums, k):
    if k > len(nums):
        return - 1
    low = max(nums)
    high = sum(nums)

    while low <= high:
        mid = (low + high) // 2

        stu = count_students(nums, mid)

        if stu > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

print(findPages([25,46,28,49,24],4)) 