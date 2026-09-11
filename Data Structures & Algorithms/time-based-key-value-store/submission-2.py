class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = []
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.key_store.get(key, [])
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (right - left) // 2 + left

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else :
                right = mid - 1
        return res
        
