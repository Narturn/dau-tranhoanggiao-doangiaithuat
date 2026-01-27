class Solution(object):
    def isValid(self, s):
        stack = []
        Par = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in Par:
                if not stack:
                    return False

                top = stack.pop()
                if top != Par[char]:
                    return False
            
            else:
                stack.append(char)
            
        return not stack