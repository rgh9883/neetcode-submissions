class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        maxLen = 0
        l, r = 0, 0
        while r < len(s):
            while s[r] in char:
                char.remove(s[l])
                l += 1
            char.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen