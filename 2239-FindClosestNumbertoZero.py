class Solution(object):
    def findClosestNumber(self, nums):
        min = abs(nums[0])
        result = nums[0]

        for i in range(1, len(nums)):
            if abs(nums[i]) < min:
                min = abs(nums[i])
                result = nums[i]
            elif abs(nums[i]) == min and nums[i] > result:
                result = nums[i]
        
        return result