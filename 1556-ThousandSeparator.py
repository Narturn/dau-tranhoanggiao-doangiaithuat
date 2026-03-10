class Solution(object):
    def thousandSeparator(self, n):
        result = ""
        string = str(n)
        count = 0

        for i in range(len(string)-1, -1, -1):
            result = string[i] + result
            count += 1
            if count % 3 == 0 and i != 0:
                result = "." + result
        return result