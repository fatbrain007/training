def findDups(nums):
    num_count = {} 
    dup_nums = []   
    
    for num in nums:
        num_count[num] = num_count.get(num, 0) + 1
    
  
    for num, count in num_count.items():
        if count > 1:
            dup_nums.append(num)
    return dup_nums


nums = [1,2,3,4,5,2,4]
print(findDups(nums))