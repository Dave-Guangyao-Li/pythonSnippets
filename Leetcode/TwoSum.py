# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# No duplicate element, you may not use the same element twice.
# You can return the answer in any order. If there are multiple pairs, return any one pair.
# If there is no such pair, return an empty array.


# Input: nums = [2,11,7,15], target = 9
# Output: [0,2]

# return : pair [0,2] target = 9

nums = [2,11,7,15]
target = 9


def returnTarget(nums, target):
       # 2 -> target - current = diff look up in hashmap
        # diff in hashmap: return pair
        # update hashmap
    res = []
    resultMap = {}
    for i, num in enumerate(nums):
        diff = target - num
        # index = nums.index(abs(diff)) # 9-7 = 2 -> index is 0
        # print(index)
        if diff in resultMap:
            res.append([resultMap[diff],i])
        resultMap[num] = i # key: num value: index
    print(resultMap)
    return res
    
 

print(returnTarget(nums, target))
            
            
    
