class MinStack:

    def __init__(self):
        self.stack = []
        self.min_e = float('inf')

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.min_e > value:
            self.min_e = value

    def pop(self) -> None:
        require_min_e_update = False
        if self.min_e == self.stack[-1]:
            require_min_e_update = True
        self.stack = self.stack[0:len(self.stack)-1]
        if require_min_e_update:
            self.min_e = float('inf')
            for i in self.stack:
                if self.min_e > i:
                    self.min_e = i

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_e
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()