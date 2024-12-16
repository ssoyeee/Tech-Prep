class MinStack:
    # Design a stack which has 4 operations - push, pop, top, getMin
    # Implement O(1) time,  O(n) space, 1 stack
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        # Determine the new minimum value
        if not self.stack:
            current_min = val # if stack is empty, new element = new min
        else:
            current_min = min(val, self.stack[-1][1])
        self.stack.append((val, current_min))
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]

    '''def __init__(self):
        self.stack = []
        self.minStack = [] #min(second) stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        #del self.stack[-1]
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #return min(self.stack)
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()'''