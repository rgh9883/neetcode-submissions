class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1Freq = {}
        freq = {}
        for i in range(len(s1)):
            s1Freq[s1[i]] = s1Freq.get(s1[i], 0) + 1
            freq[s2[i]] = freq.get(s2[i], 0) + 1
        
        if freq == s1Freq:
            return True
        l, r = 0, len(s1)-1
        while r < len(s2)-1:
            print(freq)
            r += 1
            freq[s2[r]] = freq.get(s2[r], 0) + 1
            freq[s2[l]] -= 1
            if freq[s2[l]] == 0:
                freq.pop(s2[l])
            l += 1

            if freq == s1Freq:
                return True
        return False
            