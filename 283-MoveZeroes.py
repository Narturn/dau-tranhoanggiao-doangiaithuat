class Solution(object):
    def moveZeroes(self, nums):
        n = 0
        tf = False
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[n] = nums[i]
                n += 1
                if tf:
                    nums[i] = 0
            else: 
                tf = True