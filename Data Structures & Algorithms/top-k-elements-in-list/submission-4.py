class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for n, cnt in freq.items():
            bucket[cnt].append(n)

        t = 0
        res = []
        for arr in reversed(bucket):
            for num in arr:
                res.append(num)
                t += 1
                if t == k:
                    return res
