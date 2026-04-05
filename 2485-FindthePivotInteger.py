class Solution(object):
    def pivotInteger(self, n):
        left = 1
        right = n
        mid = 0
        
        while left <= right:
            mid = (left + right) // 2
            total_mid = mid * (mid + 1) // 2
            total_n = n * (n + 1) // 2 - total_mid + mid

            if total_mid == total_n:
                return mid
            elif total_mid < total_n:
                left = mid + 1
            else:
                right = mid - 1

        return -1