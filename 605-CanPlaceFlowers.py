class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        length = len(flowerbed)

        while i < length:

            if flowerbed[i] == 0:
                # kiểm tra bên trái
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # kiểm tra bên phải
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
                    i += 2
                    continue

            i += 1

        return n <= 0