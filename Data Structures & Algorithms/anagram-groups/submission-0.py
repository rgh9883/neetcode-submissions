class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        for s in strs:
            chars = {}
            for i in range(len(s)):
                if s[i] in chars:
                    chars[s[i]] += 1
                else:
                    chars[s[i]] = 1
            key = frozenset(chars.items())
            if key in maps:
                maps[key].append(s)
            else:
                maps[key] = [s]
        return list(maps.values())