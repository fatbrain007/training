#7. How do you search a target value in arotated array?
def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) 

        if nums[mid] == target:
            return mid

      
        if nums[left] <= nums[mid]:            
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:            
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


nums = [3, 4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated_array(nums, target))  
