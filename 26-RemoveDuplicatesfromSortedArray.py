class Solution(object):
    def removeDuplicates(self, nums):
        count = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[count] = nums[read]
                count += 1

        return count