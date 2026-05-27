class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dup = set(nums)
        if len(nums) != len(no_dup):
            return True
        return False