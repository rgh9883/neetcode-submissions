class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        for key in freq:
            bucket[freq[key]].append(key)
        
        res = []
        for arr in reversed(bucket):
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res
