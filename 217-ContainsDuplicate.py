class Solution:
    def containsDuplicate(self, nums):
        v = set()
        for n in nums:
            if not n in v:
                v.add(n)
            else:
                return True
            
        return False