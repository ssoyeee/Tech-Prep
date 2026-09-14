class Logger:

    def __init__(self):
        self.last_seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_seen:
            self.last_seen[message] = timestamp + 10
            return True
        else:
            if timestamp >= self.last_seen[message]:
                self.last_seen[message] = timestamp + 10
                return True
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)