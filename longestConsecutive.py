#8. Given an unsorted array of integers,find the length of the longestconsecutive elements sequence?
def longest_consecutive(nums):
    if not nums:
        return 0

    nums_set = set(nums)
    #print(nums_set)
    longest_streak = 0

    for num in nums_set:
       
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


nums = [100, 4, 200, 1, 3, 2, 201, 5]
print(longest_consecutive(nums)) 
