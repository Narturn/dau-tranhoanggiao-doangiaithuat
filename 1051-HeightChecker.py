class Solution(object):
    def heightChecker(self, heights):
        count = 0
        expected = heights[:]

        for i in range(len(expected)):
            for j in range(i+1, len(expected)):
                if expected[i] > expected[j]:
                    expected[i], expected[j] = expected[j], expected[i]
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count