class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = (l+r) // 2
            s = 0
            for p in piles:
                s += math.ceil(p / m)
            if s > h:
                l = m + 1
            else:
                r = m
        return (l+r) // 2