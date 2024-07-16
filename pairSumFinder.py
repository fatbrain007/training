#4. How do you find all pairs of aninteger array whose sum is equal to agiven number? 
def find_pairs(nums, target_sum):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target_sum - num
        if complement in seen and num != complement:
            pairs.add(tuple(sorted((complement, num))))
        seen.add(num)

    return list(pairs)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 10
print(find_pairs(nums, target_sum)) 