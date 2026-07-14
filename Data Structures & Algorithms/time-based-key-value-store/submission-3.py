class TimeMap:

    def __init__(self):
        self.cache = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        if self.cache[key] == []:
            return ""

        values = self.cache[key]

        low = 0
        high = len(values) - 1

        ans = 0
        if timestamp < values[0][0]:
            return ""
        while low <= high:
            mid = low + (high - low) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif timestamp > values[mid][0]:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        print(values, timestamp)
        return values[ans][1]


