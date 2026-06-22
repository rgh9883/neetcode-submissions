class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Freq, s2Freq = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1
        
        ctMatch = 0
        for i in range(26):
            ctMatch += (1 if s1Freq[i] == s2Freq[i] else 0)
        
        l, r = 0, len(s1)
        while r < len(s2):
            print(s2Freq)
            if ctMatch == 26:
                return True
            
            i = ord(s2[r]) - ord('a')
            s2Freq[i] += 1
            if s1Freq[i] == s2Freq[i]:
                ctMatch += 1
            elif s1Freq[i] + 1 == s2Freq[i]:
                ctMatch -= 1
            
            j = ord(s2[l]) - ord('a')
            s2Freq[j] -= 1
            if s1Freq[j] == s2Freq[j]:
                ctMatch += 1
            elif s1Freq[j] - 1 == s2Freq[j]:
                ctMatch -= 1
            
            l += 1
            r += 1
        return ctMatch == 26
