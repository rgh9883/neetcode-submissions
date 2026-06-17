class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.timeMap.get(key, [])
        res = ""
        l, r = 0, len(pairs)-1
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] <= timestamp:
                l = m + 1
                res = pairs[m][1]
            else:
                r = m - 1
        return res
        
