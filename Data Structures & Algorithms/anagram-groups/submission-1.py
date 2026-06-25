class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freq = {}
            for c in s:
                freq[c] = freq.get(c, 0) + 1
            key = frozenset(freq.items())
            res[key].append(s)
        
        return list(res.values())
