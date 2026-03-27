class Solution(object):
    def sortEvenOdd(self, nums):
        so1 = sorted(nums[::2])
        so2 = sorted(nums[1::2], reverse = True)
        nums[::2] = so1
        nums[1::2] = so2
        return nums