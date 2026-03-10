class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        count = 0
        s = sum(nums)

        for i in nums:
            right = s - left - i

            if left == right:
                return count
            
            left += i
            count += 1

        return -1