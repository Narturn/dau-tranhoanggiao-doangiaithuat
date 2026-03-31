class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
        mid = 0

        while left <= right:
            mid = (left + right) // 2
            
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1