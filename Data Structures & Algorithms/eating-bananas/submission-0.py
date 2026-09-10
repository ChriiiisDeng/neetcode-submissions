import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1
        
        while left < right:
            mid = int((right - left) / 2) + left
            if self._canEat(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return right

    def _canEat(self, piles: List[int], k : int, h : int) -> bool:

        total_hour = 0
        for x in piles:
            time = math.ceil(x / k)
            total_hour += time

        return total_hour <= h

        