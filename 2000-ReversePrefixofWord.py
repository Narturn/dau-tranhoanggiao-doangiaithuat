class Solution(object):
    def reversePrefix(self, word, ch):
        result = []
        count = 0

        for i in word:
            result.append(i)
            if i == ch and count == 0:
                result = result[::-1]
                count += 1

        return "".join(result)