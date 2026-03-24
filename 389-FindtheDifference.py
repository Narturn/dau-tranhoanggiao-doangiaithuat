class Solution(object):
    def findTheDifference(self, s, t):
        word = {}
        for i in t:
            word[i] = word.get(i, 0) + 1
        for i in s:
            word[i] = word.get(i, 0) - 1
        for i in word:
            if word[i] == 1:
                return i