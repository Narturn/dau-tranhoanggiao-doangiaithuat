class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^\w\s]', '', s)
        s = s.lower()
        s = s.replace(" ", "")
        s = s.replace("_", "")

        if s != s[::-1]:
            return False

        return True