class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)

        words = paragraph.split()
        word = {}
        max = 0
        result = ""

        for write in words:
            if write not in banned:
                word[write] = word.get(write, 0) + 1

        for i in word:
            if word[i] > max:
                max = word[i]
                result = i

        return result