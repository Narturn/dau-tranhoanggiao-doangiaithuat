class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}

        for i in s:
            count[i] = count.get(i, 0) + 1
        
        for i in s:
            if count[s[0]] != count[i]:
                return False
        
        return True