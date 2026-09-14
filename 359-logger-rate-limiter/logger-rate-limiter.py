class Logger:

    def __init__(self):
        self.last_seen = {} # {"foo": 11}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_seen:
            # first time seeing this message
            self.last_seen[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.last_seen[message]:
                # if 10 sec have passed, allow again
                self.last_seen[message] = timestamp + 10
                return True
            return False
    # Time: O(1) per call -- dict lookup and update O(1)
    # Space: O(m) -- where n is number of uniq messages ever seen


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)