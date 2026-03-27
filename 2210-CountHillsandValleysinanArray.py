class Solution(object):
    def countHillValley(self, nums):
        count = 0
        n = []

        n.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                n.append(nums[i])

        for i in range(1, len(n) - 1):
            if n[i+1] < n[i] > n[i-1]:
                count += 1
            elif n[i+1] > n[i] < n[i-1]:
                count += 1
        
        return count