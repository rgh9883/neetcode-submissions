class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        maxF = 0
        res = 0
        l, r = 0, 0
        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxF = max(maxF, freq[s[r]])

            while (r-l+1) - maxF > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, (r-l+1))
            r += 1
        return res
