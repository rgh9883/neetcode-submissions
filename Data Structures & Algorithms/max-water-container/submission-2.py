class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        l, r = 0, len(heights)-1
        while l < r:
            c = (r - l) * min(heights[l], heights[r])
            a = max(a, c)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return a