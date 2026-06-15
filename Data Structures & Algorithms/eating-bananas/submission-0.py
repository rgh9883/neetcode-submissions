class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        l, r = 1, maxPile
        k = maxPile
        while l <= r:
            m = (l + r) // 2
            time = sum([-(-p // m) for p in piles])
            if time <= h:
                r = m - 1
                k = m
            else:
                l = m + 1
        return k