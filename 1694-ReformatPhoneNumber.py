class Solution(object):
    def reformatNumber(self, number):
        number = number.replace("-", "").replace(" ", "")
        n = len(number)
        result = []
        i = 0

        while n - i > 0:
            if n - i > 4:
                result.append(number[i:i+3])
                i += 3
            elif n - i == 4:
                result.append(number[i:i+2])
                result.append(number[i+2:i+4])
                break
            else:
                result.append(number[i:])
                break

        return "-".join(result)