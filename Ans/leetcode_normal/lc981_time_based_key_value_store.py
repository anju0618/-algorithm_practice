class TimeMap:
    def __init__(self):
        self.store = {}  # key -> list of (timestamp, value), timestamps strictly increasing

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        result = ""
        for ts, value in self.store[key]:
            if ts > timestamp:
                break
            result = value
        return result
