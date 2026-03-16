class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False

        p_to_w = {}
        w_to_p = {}

        for i in range(len(pattern)):
            pat = pattern[i]
            word = words[i]

            if pat in p_to_w:
                if p_to_w[pat] != word:
                    return False
            else:
                p_to_w[pat] = word

            if word in w_to_p:
                if w_to_p[word] != pat:
                    return False
            else:
                w_to_p[word] = pat
        
        return True