class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [(timestamp, value)]
        else:
            self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.map:
            return ''

        left = 0
        right = len(self.map[key]) - 1
        ans = ''

        while left <= right:
            mid = (left + right) // 2

            val = self.map[key][mid][1]
            ts = self.map[key][mid][0]

            if ts == timestamp:
                return val
            elif ts < timestamp:
                ans = val
                left = mid +1
            elif ts > timestamp:
                right = mid -1
        
        return ans
