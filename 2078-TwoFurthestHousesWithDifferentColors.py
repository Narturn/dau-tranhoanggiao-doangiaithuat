class Solution(object):
    def maxDistance(self, colors):
        max = 0

        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    if max < j - i:
                        max = j - i
        return max