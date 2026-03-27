class Solution(object):
    def findNumbers(self, nums):
        result = 0
        count = 0

        for i in nums:
            while i != 0:
                i /= 10
                count += 1
            if count % 2 == 0:
                result += 1
            count = 0

        return result