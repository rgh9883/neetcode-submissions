class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sChar = {}
        tChar = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            sChar[c1] = 1 + sChar.get(c1, 0)
            tChar[c2] = 1 + tChar.get(c2, 0)
        return sChar == tChar