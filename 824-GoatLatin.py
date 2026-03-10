class Solution(object):
    def toGoatLatin(self, sentence):
        vowel = "ueoaiUEOAI"
        words = sentence.split()
        result = ""

        i = 1

        for word in words:
            if word[0] in vowel:
                new_word = word + "ma"
            else:
                new_word = word[1:] + word[0] + "ma"
            
            new_word = new_word + ("a" * i)

            result = result + new_word + " "
            i = i + 1

        return result.strip()