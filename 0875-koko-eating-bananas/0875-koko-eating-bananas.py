import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        high = max(piles)
        left, right = 1, high
        count = 0

        while left <= right:
            mid = (left + right) // 2
            aux = 0
            for bananas in piles:
                if bananas > mid:
                    aux += math.ceil(bananas/mid)
                else:
                    aux += 1

            if aux <= h:
                right = mid - 1
                count = mid
            else:
                left = mid + 1
        return count