#10. How do you remove duplicates froman array in place?
def remove_duplicates(nums):
    if not nums:
        return 0

    seen = set()
    write_index = 0

    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
            nums[write_index] = nums[i]
            write_index += 1

    return write_index

nums = [1, 2, 3, "a", 1, "b", 2, "a", 4, 5, 6, 7, 3, "c"]
length = remove_duplicates(nums)
print(nums[:length])