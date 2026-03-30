class Solution(object):
    def numberGame(self, nums):
        arr = []
        Alice = 0
        Bob = 0
        
        while len(nums) != 0:
            Alice = min(nums)
            nums.remove(min(nums))
            Bob = min(nums)
            nums.remove(min(nums))
            arr.append(Bob)
            arr.append(Alice)
        
        return arr