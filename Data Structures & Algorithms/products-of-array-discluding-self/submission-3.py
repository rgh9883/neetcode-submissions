class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        val = 1
        for i in range(1, len(nums)):
            val *= nums[i-1]
            pre[i] = val
        
        val = 1
        for i in range(len(nums)-2, -1, -1):
            val *= nums[i+1]
            post[i] = val
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        
        return res