class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)
        for s in strs:
            freq = {}
            for c in s:
                freq[c] = 1 + freq.get(c, 0)
            key = frozenset(freq.items())
            grams[key].append(s)
        return list(grams.values())