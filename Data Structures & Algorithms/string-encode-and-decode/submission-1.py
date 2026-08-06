class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        i, j = 0, 1
        arr = []
        while i < len(s):
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            arr.append(s[i:j])
            i = j
        return arr