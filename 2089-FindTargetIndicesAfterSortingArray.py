class Solution(object):
    def targetIndices(self, nums, target):
        nums = sorted(nums)
        result = []

        for i in range(len(nums)):
            if target == nums[i]:
                result.append(i)
        
        return result