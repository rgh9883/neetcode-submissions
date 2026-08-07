class Solution:
    def findMin(self, nums: List[int]) -> int:
        pivot = nums[-1]
        l, r = 0, len(nums)-1
        while l < r:
            m = (l+r) // 2
            if nums[m] > pivot:
                l = m + 1
            else:
                r = m
        return nums[(l+r) // 2]
