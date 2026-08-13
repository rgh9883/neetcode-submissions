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
            r += 1
            maxLen = max(maxLen, r-l)
        return maxLen