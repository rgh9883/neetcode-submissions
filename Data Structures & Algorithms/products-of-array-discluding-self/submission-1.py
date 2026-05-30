class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        # Prefix pass
        val = 1
        for i in range(1, len(nums)):
            val *= nums[i-1]
            output[i] *= val
        
        val = 1
        for i in range(len(nums) - 2, -1, -1):
            val *= nums[i+1]
            output[i] *= val

        return output