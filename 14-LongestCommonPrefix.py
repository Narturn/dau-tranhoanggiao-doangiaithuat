class Solution:
    def longestCommonPrefix(self, strs):
        s = strs[0]

        for i in strs[1:]:
            while not i.startswith(s):
                s = s[:-1]
            if s == "":
                return ""
        return s